import json

from src.classifier import classify_persona
from src.generator import generate_response
from src.escalator import should_escalate
from src.handoff import generate_handoff_summary

from src.rag_pipeline import (
    get_collection,
    retrieve_documents
)


def main():
    """
    Run the Persona Support Agent workflow,
    including classification, retrieval,
    response generation, and escalation.
    """

    collection = get_collection()
    conversation_history = []

    print("\nPersona Support Agent Started")
    print("Type 'exit' to quit.\n")

    while True:

        user_message = input("You: ")

        if user_message.lower() == "exit":
            break

        # Persona Detection
        persona_result = classify_persona(user_message)
        persona = persona_result["persona"]

        # Retrieval
        retrieval_results = retrieve_documents(
            user_message,
            collection
        )

        retrieved_chunks = retrieval_results["documents"][0]

        conversation_history.append(user_message)

        escalation_result = should_escalate(
            user_message,
            retrieved_chunks
        )

        # Response Generation
        if escalation_result["escalate"]:

            sources = [
                metadata["source"]
                for metadata in retrieval_results["metadatas"][0]
            ]

            summary = generate_handoff_summary(
                persona=persona,
                user_message=user_message,
                conversation_history=conversation_history,
                sources=sources,
                escalation_reasons=escalation_result["reasons"]
            )

            print("\n" + "=" * 60)

            print("ESCALATION REQUIRED")

            print("\nREASONS:")

            for reason in escalation_result["reasons"]:
                print("-", reason)

            print("\nHANDOFF SUMMARY:")

            print(
                json.dumps(
                    summary,
                    indent=4
                )
            )

            print("=" * 60)

        else:

            response = generate_response(
                user_message=user_message,
                persona=persona,
                retrieved_chunks=retrieved_chunks
            )

            print("\n" + "=" * 60)

            print("PERSONA:")
            print(persona)

            print("\nSOURCES:")

            seen_sources = set()

            for metadata in retrieval_results["metadatas"][0]:

                source = metadata["source"]

                if source not in seen_sources:
                    print("-", source)
                    seen_sources.add(source)

            print("\nRESPONSE:")
            print(response)

            print("=" * 60)


if __name__ == "__main__":
    main()