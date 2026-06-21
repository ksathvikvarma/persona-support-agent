from classifier import classify_persona
from generator import generate_response

from rag_pipeline import (
    get_collection,
    retrieve_documents
)

collection = get_collection()

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

    # Response Generation
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