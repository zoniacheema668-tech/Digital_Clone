
from pathlib import Path

DATA_FOLDER = Path("data")

CHUNK_SIZE = 250
OVERLAP = 40


def create_chunks(text, chunk_size=CHUNK_SIZE, overlap=OVERLAP):
    words = text.split()
    chunks = []

    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        chunk_text = " ".join(chunk_words)

        chunks.append(chunk_text)

        if end >= len(words):
            break

        start = end - overlap

    return chunks


def load_documents():
    all_chunks = []

    for file_path in sorted(DATA_FOLDER.glob("*.md")):
        content = file_path.read_text(encoding="utf-8")
        document_chunks = create_chunks(content)

        for index, chunk in enumerate(document_chunks):
            all_chunks.append({
                "source": file_path.name,
                "chunk_id": index,
                "text": chunk
            })

    return all_chunks


if __name__ == "__main__":
    chunks = load_documents()

    print("\nDOCUMENT CHUNKING REPORT")
    print("-" * 45)

    for source in sorted(set(chunk["source"] for chunk in chunks)):
        source_chunks = [
            chunk for chunk in chunks
            if chunk["source"] == source
        ]

        print(f"{source:<20} {len(source_chunks):>5} chunks")

    print("-" * 45)
    print(f"Total chunks: {len(chunks)}")

    if chunks:
        print("\nFIRST CHUNK DETAILS")
        print("Source:", chunks[0]["source"])
        print("Chunk ID:", chunks[0]["chunk_id"])
        print("Word count:", len(chunks[0]["text"].split()))
        print("Preview:", chunks[0]["text"][:250])

