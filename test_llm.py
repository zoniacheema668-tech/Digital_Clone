from hybrid import search_hybrid
from llm import generate_answer

question = "What is my FYP title?"

results = search_hybrid(question, top_k=2)

print("\nRETRIEVED SOURCES")
print("=" * 50)

for result in results:
    print(f"Source: {result['source']}")
    print(f"Chunk ID: {result['chunk_id']}")
    print(f"Score: {result['rrf_score']:.4f}")

print("\nGENERATED ANSWER")
print("=" * 50)

answer = generate_answer(question, results)

print(answer)