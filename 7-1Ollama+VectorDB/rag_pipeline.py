from embeddings.embedder import get_embedding
from vector_store.qdrant_client import COLLECTION_NAME

def search(client, query: str, top_k: int = 3):
    query_vector = get_embedding(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=top_k
    )

    return [point.payload["text"] for point in results.points]