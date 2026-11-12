
from bm25 import search_bm25
from dense import search_dense


def search_hybrid(question, top_k=3, candidate_k=10):
    """Combine BM25 and Dense results using RRF."""

    bm25_results = search_bm25(
        question, top_k=candidate_k
    )

    dense_results = search_dense(
        question, top_k=candidate_k
    )

    combined_results = {}

    # Add BM25 rankings
    for rank, result in enumerate(bm25_results, start=1):

        key = (result["source"], result["chunk_id"])

        combined_results[key] = result.copy()
        combined_results[key]["rrf_score"] = 1 / (60 + rank)

    # Add Dense rankings
    for rank, result in enumerate(dense_results, start=1):

        key = (result["source"], result["chunk_id"])

        if key not in combined_results:
            combined_results[key] = result.copy()
            combined_results[key]["rrf_score"] = 0

        combined_results[key]["rrf_score"] += 1 / (60 + rank)

    # Sort by combined RRF score
    ranked_results = sorted(
        combined_results.values(),
        key=lambda item: item["rrf_score"],
        reverse=True
    )

    return ranked_results[:top_k]


# Test Hybrid Retrieval
if __name__ == "__main__":

    test_questions = [
        "What is my FYP title?",
        "Which university do I study at?",
        "What is my SkillBridge project?",
        "Which language model did I use in my Cloud Computing project?"
    ]

    print("\nHYBRID RETRIEVAL TEST (RRF)")
    print("-" * 55)

    for question in test_questions:

        print(f"\nQuestion: {question}")

        results = search_hybrid(question)

        for result in results:
            print(
                f"Source: {result['source']} | "
                f"Chunk ID: {result['chunk_id']} | "
                f"RRF Score: {result['rrf_score']:.5f}"
            )
