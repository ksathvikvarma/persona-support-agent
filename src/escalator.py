from src.config import ESCALATION_KEYWORDS

def should_escalate(
    user_message,
    retrieved_chunks
):
    """
    Determine whether a conversation should be
    escalated to a human support agent.
    """
    
    escalation_reasons = []

    # No retrieved content
    if not retrieved_chunks:
        escalation_reasons.append(
            "No relevant information found."
        )


    user_message_lower = user_message.lower()

    for keyword in ESCALATION_KEYWORDS:

        if keyword in user_message_lower:

            escalation_reasons.append(
                f"Sensitive issue detected: {keyword}"
            )

            break

    return {
        "escalate": len(escalation_reasons) > 0,
        "reasons": escalation_reasons
    }