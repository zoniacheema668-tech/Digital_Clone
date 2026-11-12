

import re
from rank_bm25 import BM25Okapi
from chunking import load_documents

chunks = load_documents()


def tokenize(text):
    """Convert text into lowercase word tokens."""
    return re.findall(r"\b\w+\b", text.lower())


# Tokenize all document chunks
tokenized_chunks = [
    tokenize(chunk["text"])
    for chunk in chunks
]

# Build BM25 index
bm25 = BM25Okapi(tokenized_chunks)


def search_bm25(question, top_k=3):
    """Find the most relevant chunks using BM25."""

    query_tokens = tokenize(question)
    scores = bm25.get_scores(query_tokens)

    ranked_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )[:top_k]

    results = []

    for index in ranked_indices:
        results.append({
            "source": chunks[index]["source"],
            "chunk_id": chunks[index]["chunk_id"],
            "text": chunks[index]["text"],
            "score": float(scores[index])
        })

    return results


# Testing section
if __name__ == "__main__":

    test_questions = [
        "What is my FYP title?",
        "Which university do I study at?",
        "What is my SkillBridge project?",
        "Which language model did I use in my Cloud Computing project?"
    ]

    print("\nMULTIPLE QUESTION TEST")
    print("-" * 50)

    for question in test_questions:
        print(f"\nQuestion: {question}")

        results = search_bm25(question, top_k=5)

        for result in results:
            print(
                f"Source: {result['source']} | "
                f"Chunk ID: {result['chunk_id']} | "
                f"Score: {result['score']:.4f}"
            )
