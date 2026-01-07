import ollama
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

COLLECTION_NAME = "rag_docs"

class VectorDB:
    def __init__(self):
        self.client = QdrantClient(":memory:")  # no Docker
        self.model = "nomic-embed-text"

    def get_embedding(self, text: str):
        return ollama.embeddings(
            model=self.model,
            prompt=text
        )["embedding"]

    def store_documents(self, documents: list[str]):
        embeddings = [self.get_embedding(doc) for doc in documents]

        print(f"Created {len(embeddings)} vectors of size {len(embeddings[0])}")

        self.client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=len(embeddings[0]),
                distance=Distance.COSINE
            )
        )

        points = [
            PointStruct(
                id=i,
                vector=embeddings[i],
                payload={"text": documents[i]}
            )
            for i in range(len(documents))
        ]

        self.client.upsert(
            collection_name=COLLECTION_NAME,
            points=points
        )