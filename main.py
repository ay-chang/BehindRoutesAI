from parsers.python_parser import find_python_files, extract_flask_routes_from_file
from chunking.chunker import RouteChunk
from embeddings.embedder import get_embedding
from embeddings.vector_store import store_vector, save_index

def scan_project(path):
    # 1. Walk the project, get .py files
    # 2. Extract route logic from each file
    # 3. Chunk, embed, and store in FAISS

    print("Scanning...")

    python_files = find_python_files(path)

    for file in python_files:
        routes = extract_flask_routes_from_file(file)
        for route in routes: 
            print("\n\n--- Route Found ---")
            chunk = RouteChunk(**route)
            chunk_text = chunk.to_text_chunk()
            print(chunk_text)

            # Embed + store
            embedding = get_embedding(chunk_text)
            store_vector(embedding, chunk_text)

    # Save everything at the end
    save_index()
    print("Scan complete. Vector index saved.")


def ask_question(question):
    # 1. Embed the question
    # 2. Query vector store for top-k chunks
    # 3. Format prompt and send to GPT
    # 4. Print the answer

    pass
    