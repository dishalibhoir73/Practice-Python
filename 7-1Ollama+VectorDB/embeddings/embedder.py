import ollama

EMBED_MODEL = "nomic-embed-text"

def get_embedding(text: str) -> list:
    response = ollama.embeddings(
        model=EMBED_MODEL,
        prompt=text
    )
    return response["embedding"]