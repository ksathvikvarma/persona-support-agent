from config import ESCALATION_KEYWORDS

def should_escalate(
    user_message,
    retrieved_chunks
):
    
    escalation_reasons = []

    # No retrieved content
    if not retrieved_chunks:
        escalation_reasons.append(
            "No relevant information found."
        )

    # Sensitive topics
    sensitive_keywords = ESCALATION_KEYWORDS

    user_message_lower = user_message.lower()

    for keyword in sensitive_keywords:

        if keyword in user_message_lower:

            escalation_reasons.append(
                f"Sensitive issue detected: {keyword}"
            )

            break

    return {
        "escalate": len(escalation_reasons) > 0,
        "reasons": escalation_reasons
    }