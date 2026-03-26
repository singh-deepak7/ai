import gradio as gr
import requests

API_URL = "http://localhost:8000/query"

def ask(q):
    res = requests.post(API_URL, params={"q": q})
    return res.json()["response"]

gr.Interface(
    fn=ask,
    inputs="text",
    outputs="text",
    title="Insurance AI Assistant"
).launch()