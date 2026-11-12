
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

MODEL_NAME = "llama-3.2-1b-instruct"


def generate_answer(question, retrieved_chunks):

    if not retrieved_chunks:
        return "I don't have that in my notes."

    context = "\n\n".join(
        chunk["text"] for chunk in retrieved_chunks
    )

    system_prompt = """
You are an AI digital clone of the person described in the supplied context.

Follow these rules carefully:
1. Answer in first person using I, my, and me.
2. Use ONLY the supplied context.
3. Read all supplied context before answering.
4. If the answer is explicitly stated anywhere in the context,
   you MUST provide that answer.
5. Do not say information is missing when it is present.
6. Never invent personal information.
7. Keep factual answers short and direct.
8. If the answer genuinely does not appear in the context,
   reply exactly: I don't have that in my notes.
9. Never claim to be the real person.
"""

    user_prompt = f"""
Read the context below carefully.

CONTEXT:
{context}

QUESTION:
{question}

Find the exact information that answers the question.
If it is present, give a short first-person answer.
Do not explain your search process.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=100,
        temperature=0
    )

    return response.choices[0].message.content.strip()
