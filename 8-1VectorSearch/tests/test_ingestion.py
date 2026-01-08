import ingestion

def mock_embedding(text):
    return [0.1] * 768


def test_ingest_creates_chunks_and_embeddings(monkeypatch, tmp_path):
    file = tmp_path / "policy.txt"
    file.write_text("HR policy text " * 50)

    monkeypatch.setattr(ingestion, "get_embedding", mock_embedding)

    data = ingestion.ingest(str(file))

    assert len(data) > 1
    assert "text" in data[0]
    assert "vector" in data[0]
    assert len(data[0]["vector"]) == 768
