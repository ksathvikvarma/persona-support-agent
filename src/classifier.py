from dotenv import load_dotenv
import os
import json
from google import genai
from google.genai import types


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)

response_schema = {
    "type": "OBJECT",
    "properties": {
        "persona": {
            "type": "STRING",
            "enum": [
                "Technical Expert",
                "Frustrated User",
                "Business Executive"
            ]
        },
        "confidence": {
            "type": "NUMBER"
        },
        "reasoning": {
            "type": "STRING"
        }
    },
    "required": [
        "persona",
        "confidence",
        "reasoning"
    ]
}


def classify_persona(user_message):
    """
    Classify a customer support message into one of:
    - Technical Expert
    - Frustrated User
    - Business Executive
    """

    prompt = f"""
Analyze the following customer support message and classify it into EXACTLY ONE persona.

Personas:

1. Technical Expert
   - Talks about APIs, logs, authentication, code, databases, configurations, integrations, etc.

2. Frustrated User
   - Shows frustration, urgency, anger, dissatisfaction, repeated complaints, etc.

3. Business Executive
   - Focuses on business impact, timelines, uptime, operations, revenue, ROI, or management concerns.

Customer Message:
{user_message}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=response_schema,
                temperature=0.1
            )
        )

        return json.loads(response.text)

    except Exception as e:
        return {
            "persona": "Unknown",
            "confidence": 0.0,
            "reasoning": f"Classification failed: {str(e)}"
        }


if __name__ == "__main__":
    test_message = (
        "Our operational uptime is decreasing. "
        "What is the expected resolution timeline?"
    )

    result = classify_persona(test_message)

    print(json.dumps(result, indent=4))