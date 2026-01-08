from fastapi import FastAPI
from ingestion import ingest, get_embedding
from vector_db import (
    get_client,
    create_collection,
    store_embeddings,
    retrieve_top_k,
    view_all_vectors
)

app = FastAPI()
client = get_client()


@app.post("/ingest")
def ingest_data():
    data = ingest("policies.txt")

    vector_size = len(data[0]["vector"])
    create_collection(client, vector_size)
    store_embeddings(client, data)

    return {"status": "ingestion completed", "chunks": len(data)}


@app.post("/search")
def search(query: str):
    query_vector = get_embedding(query)
    results = retrieve_top_k(client, query_vector)

    return {"results": results}


@app.get("/view")
def view_db():
    return view_all_vectors(client)
