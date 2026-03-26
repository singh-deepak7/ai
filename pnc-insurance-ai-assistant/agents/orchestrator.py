from agents.planner import plan
from agents.researcher import research
from agents.synthesizer import synthesize


def run_multi_agent(query: str):
    print("🧠 Planning...")
    steps = plan(query)

    print(f"📌 Sub-questions: {steps}")

    results = []
    for step in steps:
        print(f"🔍 Researching: {step}")
        answer = research(step)
        results.append(answer)

    print("🧩 Synthesizing final answer...")
    final_answer = synthesize(query, results)

    return final_answer