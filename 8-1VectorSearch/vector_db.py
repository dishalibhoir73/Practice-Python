from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

COLLECTION_NAME = "company_policies"
TOP_K = 3


def get_client():
    return QdrantClient(path="./qdrant_data")


def create_collection(client, vector_size: int):
    existing = [c.name for c in client.get_collections().collections]
    if COLLECTION_NAME not in existing:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )


def store_embeddings(client, data: list[dict]):
    points = [
        PointStruct(
            id=item["id"],
            vector=item["vector"],
            payload={"text": item["text"]}
        )
        for item in data
    ]

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )


def retrieve_top_k(client, query_vector: list, k: int = TOP_K):
    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=k,
        with_payload=True
    )

    return [
        {
            "score": float(point.score),
            "text": point.payload.get("text", "")
        }
        for point in response.points
    ]


def view_all_vectors(client):
    response = client.query_points(
        collection_name=COLLECTION_NAME,
        prefetch=[],          
        limit=100,
        with_payload=True
    )

    return [
        {
            "id": point.id,
            "text": point.payload.get("text", "")
        }
        for point in response.points
    ]
