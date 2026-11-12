# Digital Clone – Hybrid Retrieval-Augmented Generation (RAG) Project Report

**GitHub Repository:** https://github.com/zoniacheema668-tech/Digital_Clone  
**Live Hugging Face Space:** https://huggingface.co/spaces/zoeeyyy/Digital-Clone

## 1. Introduction

The purpose of this project is to develop a Digital Clone chatbot that can answer questions about me using my personal documents. The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from a knowledge base before generating an answer.

I implemented three retrieval approaches: BM25, Dense Retrieval, and Hybrid Retrieval. The application was developed using Python and Gradio and deployed publicly on Hugging Face Spaces.

## 2. Knowledge Base Selection

I prepared seven Markdown documents containing personal, academic, and project-related information.

| Document | Information included |
|---|---|
| bio.md | Personal background and interests |
| cv.md | Education and skills |
| faq.md | Frequently asked questions and answers |
| projects.md | Academic and practical projects |
| opinions.md | Personal opinions and preferences |
| study_habits.md | Learning habits and study preferences |
| fyp.md | Final Year Project details |

I selected these documents because they provide different types of information about me. This allows the chatbot to answer questions about my education, projects, preferences, and academic work.

## 3. Retrieval Methods

The project implements three retrieval methods:

**BM25:** Uses keyword-based matching to find documents containing terms related to the user's question.

**Dense Retrieval:** Uses sentence embeddings and semantic similarity to find information based on meaning, even when the question uses different wording.

**Hybrid Retrieval:** Combines keyword-based and semantic retrieval to improve the ranking of relevant information.

## 4. Testing and Results

I tested the chatbot with questions covering my academic background, projects, learning preferences, and Final Year Project. The following table summarizes the results observed during testing.

| Test Question | BM25 | Dense | Hybrid |
|---|---|---|---|
| What is my FYP title? | Keyword retrieval implemented | Semantic retrieval implemented | Correct answer: Exam Integrity System |
| Which university do I study at? | University-related information retrieved | Semantic matching used | Semantic and keyword retrieval combined |
| What is my SkillBridge project? | SkillBridge information retrieved | SkillBridge information retrieved | Relevant project information retrieved |
| Which language model did I use in my Cloud Computing project? | Relevant project information retrieved | Semantic retrieval used | Hybrid retrieval used |
| What database project did I develop and which entities does it contain? | Failed to retrieve the exact information | Correctly identified SkillBridge and its eight entities | Correctly identified SkillBridge; exact passage ranked first |
| What is the name of my nine-screen food delivery application prototype? | Keyword-based retrieval available | Semantic retrieval available | Correct answer: EatEasy |
| What approach helps me master unfamiliar material? | Keyword-based retrieval available | Semantic retrieval available | Correct answer described my preference for practical implementation |
| What problems does my Exam Integrity System identify or manage? | Keyword-based retrieval available | Semantic retrieval available | Correctly retrieved hall overcapacity, duplicate roll numbers, and hall unavailability |

### Important observations

- BM25 was useful for matching specific terms but did not always rank the required information effectively.
- Dense retrieval successfully identified the SkillBridge project and its eight entities.
- Hybrid retrieval ranked the exact SkillBridge entity passage first and successfully retrieved the Exam Integrity System information.
- The Hybrid retrieval test for the Exam Integrity System returned the correct source and content, although the later Gemini answer-generation request encountered a temporary 503 service error.

## 5. Rare Keyword Test

**Question:** What is the name of my nine-screen food delivery application prototype?

**Retrieved answer:** EatEasy.

The chatbot successfully identified the project name from the knowledge base. This test demonstrated its ability to retrieve a specific project detail.

## 6. Paraphrased Question Test

**Question:** What approach helps me master unfamiliar material?

**Retrieved answer:** I prefer learning through practical implementation rather than memorizing definitions or simply reading theoretical explanations.

This test demonstrated that the chatbot could retrieve information based on the meaning of a question rather than relying only on exact keyword matching.

## 7. Failure Case

During testing, BM25 did not retrieve the exact information required for the SkillBridge database question. The chatbot responded that the information was not available in its notes, even though the relevant details existed in the knowledge base.

This showed that keyword-based retrieval can sometimes fail when the important information is not ranked highly enough for a particular query.

Another temporary issue occurred when the Gemini API returned a 503 UNAVAILABLE error because of high demand. The retrieval process still displayed relevant chunks, but answer generation could not complete for that request.

## 8. Possible Improvements

The system could be improved by:

- Adjusting chunk size and overlap to preserve related information.
- Improving retrieval ranking and the balance between keyword and semantic results.
- Adding better error handling for temporary API failures.
- Expanding the knowledge base with more personal and academic information.

## 9. Conclusion

The Digital Clone project demonstrates how Retrieval-Augmented Generation can be used to build a chatbot that answers questions using personal documents. By implementing BM25, Dense, and Hybrid retrieval, I explored different ways of finding relevant information.

Hybrid retrieval was particularly useful in the tested examples because it combines keyword matching with semantic understanding. The project also provided practical experience in document processing, text chunking, embeddings, retrieval, API integration, and deployment using Hugging Face Spaces.
