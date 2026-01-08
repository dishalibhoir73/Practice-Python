import ollama
from pathlib import Path

EMBED_MODEL = "nomic-embed-text"


def load_txt(file_path: str) -> str:
    return Path(file_path).read_text(encoding="utf-8")


def chunk_text(text: str, chunk_size: int = 100, overlap: int = 40) -> list[str]:
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap

    return chunks


def get_embedding(text: str) -> list:
    response = ollama.embeddings(
        model=EMBED_MODEL,
        prompt=text
    )
    return response["embedding"]


def ingest(file_path: str):
    text = load_txt(file_path)
    chunks = chunk_text(text)

    embeddings = []
    for idx, chunk in enumerate(chunks):
        vector = get_embedding(chunk)
        embeddings.append({
            "id": idx,
            "text": chunk,
            "vector": vector
        })

    print(f"Chunks created: {len(chunks)}")
    print(f"Embedding dimension: {len(embeddings[0]['vector'])}")

    return embeddings
