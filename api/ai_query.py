def load_kpis():
    with open("data/processed/kpis.txt", "r") as f:
        return f.read()


def build_prompt(question, context):
    prompt = f"""
You are a data analyst.

Context:
{context}

Question:
{question}

Answer in a clear and concise way.
"""
    return prompt


def fake_ai_response(prompt):
    # Simulación de AI (luego conectamos real)
    return "This is a simulated AI response based on the provided data."


def ask_ai(question):
    context = load_kpis()
    prompt = build_prompt(question, context)
    response = fake_ai_response(prompt)
    return response


if _name_ == "_main_":
    question = input("Ask a business question: ")
    answer = ask_ai(question)
    print("\nAI Response:")
    print(answer)
