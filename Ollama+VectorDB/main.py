import ollama
from vector import VectorDB

def load_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    vectordb = VectorDB()
    context = load_txt(r"D:\Practice-Python\Ollama+VectorDB\policies.txt")

    while True:
        query = input("Ask a question (type 'q' to quit): ")

        if query.lower() == "q":
            break

        prompt = f"""
Answer the question ONLY using the context below.

Context:
{context}

Question:
{query}

Answer:
"""

        response = ollama.generate(
            model="llama3.2",
            prompt=prompt
        )

        answer = response["response"]
        print("\nAnswer:\n", answer)
        print("-" * 40)

        vectordb.store_documents([
            f"Question: {query}",
            f"Answer: {answer}"
        ])

if __name__ == "__main__":
    main()