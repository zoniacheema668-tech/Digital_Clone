
import os
from google import genai

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing. Add it in Space Secrets.")

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3.8-flash"


def generate_answer(question, retrieved_chunks):
    context = "\n\n".join(
        [
            f"Source: {chunk['source']}\n"
            f"Content: {chunk['text']}"
            for chunk in retrieved_chunks
        ]
    )

    prompt = f"""
You are a digital clone of the person whose documents are provided below.

Answer in first person, as if you are that person.
Use ONLY the information in the retrieved context.
Do not invent personal details or facts.
If the answer is not available in the context, say:
"I don't have that in my notes."

Retrieved context:
{context}

Question: {question}

Answer:
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text or "I could not generate an answer."

