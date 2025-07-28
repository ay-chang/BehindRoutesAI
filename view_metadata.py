import pickle

with open("vector_store/metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

for i, chunk in enumerate(metadata):
    print(f"\n--- Chunk {i + 1} ---\n{chunk}")
