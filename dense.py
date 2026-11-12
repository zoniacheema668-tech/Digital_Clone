
import numpy as np
from chunking import load_documents
from pathlib import Path

# Load document chunks
chunks = load_documents()

# Load existing embeddings without loading the model
if Path("embeddings.npy").exists():
    embeddings = np.load("embeddings.npy")
    print("\nExisting embeddings loaded successfully!")
else:
    from sentence_transformers import SentenceTransformer

    print("\nGenerating document embeddings...")

    model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=True
    )

    np.save("embeddings.npy", embeddings)
    print("\nEmbeddings saved successfully!")

print("Total chunks:", len(chunks))
print("Embedding shape:", embeddings.shape)

# Load the model only when Dense retrieval is actually requested
model = None

def get_model():
    global model

    if model is None:
        from sentence_transformers import SentenceTransformer

        print("\nLoading Dense retrieval model...")
        model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

    return model


def search_dense(question, top_k=3):
    """Find relevant chunks using semantic similarity."""

    embedding_model = get_model()

    query_embedding = embedding_model.encode(
        [question],
        convert_to_numpy=True,
        normalize_embeddings=True
    )[0]

    scores = embeddings @ query_embedding
    ranked_indices = np.argsort(scores)[::-1][:top_k]

    results = []

    for index in ranked_indices:
        results.append({
            "source": chunks[index]["source"],
            "chunk_id": chunks[index]["chunk_id"],
            "text": chunks[index]["text"],
            "score": float(scores[index])
        })

    return results


if __name__ == "__main__":

    test_questions = [
        "What is my FYP title?",
        "Which university do I study at?",
        "What is my SkillBridge project?",
        "Which language model did I use in my Cloud Computing project?"
    ]

    print("\nDENSE RETRIEVAL TEST")
    print("-" * 50)

    for question in test_questions:
        print(f"\nQuestion: {question}")

        results = search_dense(question, top_k=3)

        for result in results:
            print(
                f"Source: {result['source']} | "
                f"Chunk ID: {result['chunk_id']} | "
                f"Score: {result['score']:.4f}"
            )
