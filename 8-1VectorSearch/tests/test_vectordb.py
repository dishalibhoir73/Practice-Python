import vector_db

def test_store_and_retrieve_vectors():
    client = vector_db.get_client()
    vector_size = 768

    vector_db.create_collection(client, vector_size)

    data = [{
        "id": 1,
        "text": "Leave policy",
        "vector": [0.1] * vector_size
    }]

    vector_db.store_embeddings(client, data)

    results = vector_db.retrieve_top_k(
        client,
        query_vector=[0.1] * vector_size,
        k=1
    )

    assert len(results) == 1
    assert "text" in results[0]
