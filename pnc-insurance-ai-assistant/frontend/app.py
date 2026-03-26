import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/query"

def ask(query):
    res = requests.post(API_URL, params={"q": query})
    data = res.json()

    answer = data.get("response", "No answer returned")

    sources = "\n".join([
        f"📄 {s}" for s in data.get("sources", [])
    ])

    trace = "\n".join([
        f"{t}" for t in data.get("trace", [])
    ])

    return answer, sources, trace


with gr.Blocks() as demo:
    gr.Markdown("# 🧠 AI Insurance Assistant (Multi-Agent)")

    query = gr.Textbox(label="Ask a question")

    with gr.Row():
        answer = gr.Textbox(label="💬 Answer", lines=6)

    with gr.Row():
        sources = gr.Textbox(label="📚 Sources", lines=6)
        trace = gr.Textbox(label="🧠 Agent Trace", lines=6)

    btn = gr.Button("Ask")

    btn.click(ask, inputs=query, outputs=[answer, sources, trace])

demo.launch()