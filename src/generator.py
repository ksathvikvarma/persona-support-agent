from dotenv import load_dotenv
import os

from google import genai

from src.config import GENERATION_MODEL

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)


def generate_response(user_message, persona, retrieved_chunks):
    """
    Generate a persona-aware support response using
    retrieved knowledge base context.
    """

    # Convert list of chunks into a single context block
    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
    You are an AI customer support assistant.

    Detected Persona:
    {persona}

    Knowledge Base Context:
    {context}

    Customer Question:
    {user_message}

    Instructions:
    - Answer ONLY using the provided knowledge base context.
    - Do not make up information.
    - Adapt the tone based on the persona.

    Persona Styles:

    Technical Expert:
    - Detailed
    - Technical
    - Step-by-step explanation

    Frustrated User:
    - Empathetic
    - Reassuring
    - Professional
    - Avoid excessive emotional language

    Business Executive:
    - Concise
    - Business-focused
    - Minimal technical jargon

    Generate the final response.
    """

    try:
        response = client.models.generate_content(
            model=GENERATION_MODEL,
            contents=prompt
        )

        return response.text

    except Exception as e:

        if "429" in str(e):
            return (
                "The AI service has reached its usage limit. "
                "Please try again later."
            )

        return (
            "Unable to generate a response at this time."
        )


if __name__ == "__main__":

    retrieved_chunks = [
        "Users may reset their password using the Forgot Password option.",
        "Accounts are automatically unlocked after 15 minutes.",
        "If the issue persists, contact customer support."
    ]

    result = generate_response(
        user_message="I cannot access my account.",
        persona="Frustrated User",
        retrieved_chunks=retrieved_chunks
    )

    print("\nGENERATED RESPONSE:\n")
    print(result)