from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

user_message = "Our production API returns 401 unauthorized."

prompt = f"""
Classify the following customer message into ONE category:

1. Technical Expert
2. Frustrated User
3. Business Executive

Customer Message:
{user_message}

Return only the category name.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)