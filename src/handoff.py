def generate_handoff_summary(
    persona,
    user_message,
    conversation_history,
    sources,
    escalation_reasons
):

    summary = {
        "persona": persona,
        "issue": user_message,
        "conversation_history": conversation_history,
        "documents_used": list(set(sources)),
        "attempted_steps": [
            "Knowledge base retrieval",
            "AI response generation"
        ],
        "recommendation": "; ".join(escalation_reasons)
    }

    return summary