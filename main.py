from parsers.python_parser import *

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
            for key, value in route.items():
                print(f"{key}: {value}")



def ask_question(question):
    # 1. Embed the question
    # 2. Query vector store for top-k chunks
    # 3. Format prompt and send to GPT
    # 4. Print the answer

    pass
    