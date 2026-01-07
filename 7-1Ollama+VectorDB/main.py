from fastapi import FastAPI
from vector_store.qdrant_client import get_client, create_collection, COLLECTION_NAME
from embeddings.embedder import get_embedding
from rag_pipeline import search
from qdrant_client.models import PointStruct

app = FastAPI()
client = get_client()

# setup on startup
@app.on_event("startup")
def setup():
    sample_vector = get_embedding("test")
    create_collection(client, len(sample_vector))

    with open("policies.txt", "r") as f:
        text = f.read()

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=1,
                vector=get_embedding(text),
                payload={"text": text}
            )
        ]
    )

@app.get("/query")
def query_policy(q: str):
    results = search(client, q)
    return {"results": results}