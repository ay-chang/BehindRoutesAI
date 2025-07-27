# embeddings/embedder.py

import openai
import os
from typing import List

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_embedding(text: str) -> List[float]:
    """Call OpenAI API to get the embedding for a text chunk."""
    response = openai.Embedding.create(
        model="text-embedding-3-small",
        input=text
    )
    return response["data"][0]["embedding"]
