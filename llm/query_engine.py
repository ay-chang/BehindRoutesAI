from openai import OpenAI
import os
from dotenv import load_dotenv
from embeddings.vector_store import load_index, query_vector, get_chunk_by_index
from embeddings.embedder import get_embedding

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
GPT_MODEL = "gpt-3.5-turbo"  # "gpt-3.5-turbo" for cheaper dev, look into other models

def run_rag_pipeline(user_question: str, top_k: int = 4) -> str:
    # Step 1: Load the index and metadata
    load_index()

    # Step 2: Embed the user's question
    question_embedding = get_embedding(user_question)

    # Step 3: Retrieve top-k matching chunks
    results = query_vector(question_embedding, top_k=top_k)
    top_chunks = [get_chunk_by_index(idx) for idx, _ in results]

    # Step 4: Format the prompt
    context = "\n\n---\n\n".join(top_chunks)
    prompt = f"""
You are an assistant that helps developers understand backend API logic.

Based on the following backend route code snippets, answer the question:

[QUESTION]
{user_question}

[CONTEXT]
{context}

Respond in clear, concise language, referencing routes or functions if needed.
""".strip()

    # Step 5: Send to OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content

