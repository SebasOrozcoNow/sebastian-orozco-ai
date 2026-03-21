import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

def load_kpis():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, "data", "processed", "kpis.txt")

    with open(file_path, "r") as f:
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
        model="claude-haiku-4-5-20251001",
        max_tokens=300,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text


if __name__ == "__main__":
    q = input("Ask: ")
    print(ask_ai(q))
