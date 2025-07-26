# BehindRoutesAI

BehindRoutesAI is a tool designed to automatically extract, analyze, and embed API endpoint logic from Python web projects (e.g., Flask). It enables developers to build powerful AI-assisted tools such as documentation generators, intelligent query assistants, and code understanding interfaces by transforming backend route logic into semantically searchable vectors.

## What This Project Does

BehindRoutesAI walks through a Python-based project directory, identifies web API routes (currently supports Flask), and parses the logic inside those routes. It then chunks the relevant logic into manageable text segments, embeds them using a language model, and stores the results in a FAISS vector database for fast semantic search.

This setup allows for intelligent querying of the API logic, paving the way for agentic tools or natural language interfaces to understand and interact with your backend.

## Project Structure and Flow

The core pipeline of the project consists of the following stages:

### 1. Parsing Python Files

- Recursively scans the given project directory for `.py` files.
- Identifies API route definitions by parsing Flask decorators (e.g., `@app.route(...)`).
- For each matched route, captures the function body and relevant context.

### 2. Chunking the Logic

- Breaks the extracted route logic into smaller chunks of code and text.
- Improves granularity and efficiency for embedding and search.

### 3. Embedding the Chunks

- Each chunk is embedded using a language model (such as OpenAI’s embedding models).
- The resulting vectors are indexed using FAISS, a high-performance vector database.

### 4. Semantic Search (Query Phase)

- Enables natural language querying against the embedded route logic.
- Retrieves the most semantically relevant chunks from the FAISS index.
- Supports intelligent documentation, debugging, and agent-based use cases.

## Future Features

- **GraphQL and FastAPI Support**: Extend parsing capabilities to more frameworks.
- **Frontend Interface**: Build a visual UI for exploring routes and querying results.
- **Agent Support**: Integrate with agent frameworks for deeper AI interaction.
- **Auto-Docs Generator**: Automatically generate endpoint documentation using LLMs.
- **Smart Change Tracking**: Detect and re-embed only modified files.
- **Authentication Context Extraction**: Automatically classify routes by auth level.
