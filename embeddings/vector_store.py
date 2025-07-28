# embeddings/vector_store

import faiss
import pickle
import os
import numpy as np
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


# Add an embedding to our index as well as attaching metadata
def store_vector(embedding: List[float], chunk_id: str):
    global metadata
    embedding_np = np.array([embedding], dtype=np.float32)
    index.add(embedding_np)
    metadata.append(chunk_id)

# Saves the vector embeddings and metadata to disk so we don’t lose them
# between runs, this way we dont have to re-embed everything everytime we run 
# the app, saving costs.
def save_index():
    faiss.write_index(index, INDEX_PATH)
    with open(META_PATH, "wb") as f:
        pickle.dump(metadata, f)

# Reads the FAISS index and metadata back into memory so users can Use the stored 
# vectors for search and map those vectors back to the original code chunks
def load_index():
    global index, metadata
    if os.path.exists(INDEX_PATH):
        index = faiss.read_index(INDEX_PATH)
    if os.path.exists(META_PATH):
        with open(META_PATH, "rb") as f:
            metadata = pickle.load(f)

# This performs the similarity search and gives you the top matching vectors
def query_vector(vector: List[float], top_k: int = 5) -> List[Tuple[int, float]]:
    np_vector = np.array([vector]).astype("float32")  # wrap + convert to correct type
    distances, indices = index.search(np_vector, top_k)
    return list(zip(indices[0], distances[0]))

def get_chunk_by_index(i: int) -> str:
    return metadata[i]
