import streamlit as st

from src.classifier import classify_persona
from src.generator import generate_response
from src.escalator import should_escalate
from src.handoff import generate_handoff_summary
from src.rag_pipeline import (
    get_collection,
    retrieve_documents
)

st.set_page_config(
    page_title="Persona Support Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Persona Support Agent")

st.write(
    "AI-powered customer support assistant using "
    "Persona Classification and RAG."
)

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

@st.cache_resource
def load_collection():
    return get_collection()

collection = load_collection()

user_message = st.text_area(
    "Enter your question",
    height=120
)

if st.button("Submit"):

    if user_message.strip():

        persona_result = classify_persona(
            user_message
        )

        persona = persona_result["persona"]

        retrieval_results = retrieve_documents(
            user_message,
            collection
        )

        retrieved_chunks = retrieval_results["documents"][0]

        st.session_state.conversation_history.append(
            user_message
        )

        escalation_result = should_escalate(
            user_message,
            retrieved_chunks
        )

        st.subheader("Detected Persona")
        st.info(persona)

        st.subheader("Sources")

        seen_sources = set()

        for metadata in retrieval_results["metadatas"][0]:

            source = metadata["source"]

            if source not in seen_sources:
                st.write(f"- {source}")
                seen_sources.add(source)

        if escalation_result["escalate"]:

            sources = [
                metadata["source"]
                for metadata in retrieval_results["metadatas"][0]
            ]

            summary = generate_handoff_summary(
                persona=persona,
                user_message=user_message,
                conversation_history=st.session_state.conversation_history,
                sources=sources,
                escalation_reasons=escalation_result["reasons"]
            )

            st.error("Escalation Required")

            st.subheader("Reasons")

            for reason in escalation_result["reasons"]:
                st.write(f"- {reason}")

            st.subheader("Handoff Summary")
            st.json(summary)

        else:

            response = generate_response(
                user_message=user_message,
                persona=persona,
                retrieved_chunks=retrieved_chunks
            )

            st.subheader("Response")
            st.write(response)