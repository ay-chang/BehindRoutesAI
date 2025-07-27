# embeddings/vector_store

import faiss
import pickle
import os
from typing import List, Tuple

EMBEDDING_DIM = 1536  # For OpenAI's text-embedding-3-small

# Paths
INDEX_PATH = "vector_store/faiss.index"
META_PATH = "vector_store/metadata.pkl"

# Ensure directory exists
os.makedirs("vector_store", exist_ok=True)

# Initialize index
index = faiss.IndexFlatL2(EMBEDDING_DIM)
metadata: List[str] = []  # Will store the text chunk or chunk ID

def store_vector(embedding: List[float], chunk_id: str):
    global metadata
    index.add([embedding])
    metadata.append(chunk_id)

# Saves the vectors and metadata to disk so you don’t lose them between runs
def save_index():
    faiss.write_index(index, INDEX_PATH)
    with open(META_PATH, "wb") as f:
        pickle.dump(metadata, f)


def load_index():
    global index, metadata
    if os.path.exists(INDEX_PATH):
        index = faiss.read_index(INDEX_PATH)
    if os.path.exists(META_PATH):
        with open(META_PATH, "rb") as f:
            metadata = pickle.load(f)

# This performs the similarity search and gives you the top matching vectors
def query_vector(vector: List[float], top_k: int = 5) -> List[Tuple[int, float]]:
    """Return (index, distance) pairs for the top_k most similar vectors"""
    distances, indices = index.search([vector], top_k)
    return list(zip(indices[0], distances[0]))

def get_chunk_by_index(i: int) -> str:
    return metadata[i]
