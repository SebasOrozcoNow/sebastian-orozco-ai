import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def load_kpis():
    with open("data/processed/kpis.txt", "r") as f:
        return f.read()


def build_prompt(question, context):
    return f"""
You are a data analyst.

Context:
{context}

Question:
{question}

Answer clearly and professionally.
"""


def ask_ai(question):
    context = load_kpis()
    prompt = build_prompt(question, context)

    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=300,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text


if __name__ == "__main__":
    q = input("Ask: ")
    print(ask_ai(q))
