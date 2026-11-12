import os
import gradio as gr

from bm25 import search_bm25
from dense import search_dense
from hybrid import search_hybrid
from llm import generate_answer


def run_chat(question, mode):

    if not question or not question.strip():
        return (
            "Please enter a question first.",
            "",
            "Waiting for your question."
        )

    try:
        question = question.strip()

        print(f"\nNew question: {question}")
        print(f"Retrieval mode: {mode}")

        # Choose retrieval method
        if mode == "BM25":
            results = search_bm25(question, top_k=3)

        elif mode == "Dense":
            results = search_dense(question, top_k=3)

        else:
            results = search_hybrid(question, top_k=3)

        if not results:
            return (
                "I couldn't find relevant information in my knowledge base.",
                "",
                "No relevant chunks were retrieved."
            )

        # Generate the answer
        answer = generate_answer(question, results)

        # Format retrieved knowledge
        details = ""

        for index, result in enumerate(results, start=1):

            score = result.get(
                "rrf_score",
                result.get("score", 0)
            )

            details += (
                f"### Retrieved Chunk {index}\n"
                f"**Source:** `{result['source']}`\n\n"
                f"**Chunk ID:** {result['chunk_id']}\n\n"
                f"**Retrieval Score:** {score:.4f}\n\n"
                f"**Content:**\n\n"
                f"{result['text']}\n\n"
                f"---\n\n"
            )

        print("Answer generated successfully.")

        return (
            answer,
            details,
            f"Completed successfully using **{mode}** retrieval."
        )

    except Exception as error:

        print(f"ERROR in run_chat: {error}")

        return (
            f"**Something went wrong:**\n\n`{str(error)}`",
            "",
            "Request failed. Check the error above and your terminal."
        )


custom_css = """
.gradio-container {
    max-width: 1150px !important;
    margin: auto !important;
}

#hero {
    padding: 35px;
    border-radius: 20px;
    background: linear-gradient(120deg, #29234d, #172c48, #173b43);
    border: 1px solid #514b78;
    margin-bottom: 18px;
}

#hero h1 {
    font-size: 35px;
    margin-bottom: 8px;
    color: white;
}

#hero p {
    color: #dedcf5;
    font-size: 15px;
}

#disclaimer {
    padding: 12px 18px;
    border-radius: 10px;
    background: #332b19;
    border: 1px solid #79612d;
    color: #f4d99a;
    margin-bottom: 20px;
}

#ask-btn {
    min-height: 52px;
    font-size: 17px;
    font-weight: 700;
}

#answer-panel {
    border: 1px solid #514b78;
    border-radius: 15px;
    padding: 18px;
    min-height: 150px;
}

#status {
    font-size: 13px;
}
"""


with gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="violet",
        secondary_hue="blue",
        neutral_hue="slate"
    ),
    css=custom_css,
    title="My Digital Clone"
) as demo:

    gr.HTML("""
    <div id="hero">
        <h1>✦ My Digital Clone</h1>
        <p>
            An AI-powered personal knowledge assistant.
            Explore my background, projects, skills and learning journey.
        </p>
    </div>
    """)

    gr.HTML("""
    <div id="disclaimer">
        <b>ⓘ AI Disclaimer:</b>
        This is an AI clone, not the real person.
        Answers are generated from my personal knowledge base.
    </div>
    """)

    gr.Markdown("## Ask me something")

    with gr.Row():

        with gr.Column(scale=3):

            question = gr.Textbox(
                label="Your Question",
                placeholder="e.g. What is my Final Year Project?",
                lines=3
            )

        with gr.Column(scale=1):

            mode = gr.Dropdown(
                choices=["Hybrid", "BM25", "Dense"],
                value="Hybrid",
                label="Retrieval Method",
                interactive=True
            )

    submit = gr.Button(
        "✦  Generate Answer",
        variant="primary",
        elem_id="ask-btn"
    )

    gr.Examples(
        examples=[
            ["What is my FYP title?", "Hybrid"],
            ["Which university do I study at?", "Hybrid"],
            ["What is my SkillBridge project?", "Dense"],
            ["Which language model did I use in my Cloud Computing project?", "BM25"]
        ],
        inputs=[question, mode],
        label="Try these example questions"
    )

    gr.Markdown("## Your Answer")

    answer = gr.Markdown(
        value="Your answer will appear here after you ask a question.",
        elem_id="answer-panel"
    )

    status = gr.Markdown(
        "Ready when you are.",
        elem_id="status"
    )

    with gr.Accordion(
        "View Retrieved Knowledge & Sources",
        open=False
    ):
        retrieved = gr.Markdown()

    submit.click(
        fn=run_chat,
        inputs=[question, mode],
        outputs=[answer, retrieved, status],
        show_progress="full"
    )

    question.submit(
        fn=run_chat,
        inputs=[question, mode],
        outputs=[answer, retrieved, status],
        show_progress="full"
    )


if __name__ == "__main__":
    demo.queue().launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 10000))
)
