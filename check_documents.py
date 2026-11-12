from pathlib import Path

DATA_FOLDER = Path("data")

total_words = 0

print("\nKNOWLEDGE BASE REPORT")
print("-" * 45)

for file_path in sorted(DATA_FOLDER.glob("*.md")):
    content = file_path.read_text(encoding="utf-8")

    words = content.split()
    word_count = len(words)

    total_words += word_count

    print(f"{file_path.name:<20} {word_count:>6} words")

print("-" * 45)
print(f"{'TOTAL WORDS':<20} {total_words:>6}")
print(f"Total documents: {len(list(DATA_FOLDER.glob('*.md')))}")