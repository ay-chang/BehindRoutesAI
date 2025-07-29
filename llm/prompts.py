# llm/prompts.py

def build_rag_prompt(question: str, context: str) -> str:
    return f"""
You are an assistant that helps developers understand backend API logic.

Based on the following backend route code snippets, answer the question:

[QUESTION]
{question}

[CONTEXT]
{context}

Respond in clear, concise language, referencing routes or functions if needed.
""".strip()
