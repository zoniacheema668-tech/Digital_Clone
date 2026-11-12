# Digital Clone – Hybrid RAG Project Report

**GitHub Repository:** https://github.com/zoniacheema668-tech/Digital_Clone

**Live Hugging Face Space:** https://huggingface.co/spaces/zoeeyyy/Digital-Clone

### 1. Knowledge Base Selection

I created a personal knowledge base using seven Markdown documents: bio, CV, FAQ, projects, opinions, study habits, and FYP. These documents contain my academic background, technical interests, projects, learning preferences, and personal opinions. I selected them to help the chatbot answer questions based on my actual information rather than generating unsupported details.

### 2. Retrieval Mode Comparison

| Test Question | BM25 | Dense | Hybrid | Best Mode |
|---|---|---|---|---|
| What is my FYP title? | Correct | Not tested | Correct | Hybrid |
| What database project did I develop and which entities does it contain? | Incorrect | Correct | Correct | Hybrid |
| What is the name of my nine-screen food delivery application prototype? | Not tested | Not tested | Correct | Hybrid |
| What kind of work do I prefer when learning something new? | Not tested | Not tested | Correct | Hybrid |

Hybrid performed well in the tested questions by combining keyword-based and semantic retrieval. However, more testing would be required to establish that it is consistently the best mode.

### 3. Rare Keyword Test

**Question:** What is the name of my nine-screen food delivery application prototype?

**Expected Answer:** EatEasy.

**Result:** The chatbot correctly identified EatEasy and retrieved the relevant passage from `projects.md`.

### 4. Paraphrased Question Test

**Question:** What kind of work do I prefer when learning something new?

**Expected Answer:** Practical implementation rather than memorizing definitions or only reading theoretical explanations.

**Result:** The chatbot generated the correct answer and retrieved supporting information from `bio.md`.

### 5. Failure Case

During BM25 testing, the question about the SkillBridge database project and its entities did not return the exact entity list in the top retrieved chunks. The chatbot responded that the information was unavailable. This happened because BM25 mainly relies on keyword matching and can struggle when the question wording differs from the document wording.

### 6. Possible Improvement

The system could be improved by testing different chunk sizes and retrieval weights, adding more paraphrased questions to the FAQ, and evaluating retrieval accuracy on a larger set of questions. This could improve the relevance of retrieved information and reduce incorrect unavailable responses.
