import streamlit as st
from models.model_loader import load_models
from agents.base_agent import LLMAgent
from agents.evaluator import EvaluatorAgent
import numpy as np
import pandas as pd

def run(query):
    model_ids = [
        "Qwen/Qwen1.5-1.8B",
        "google/gemma-3-1b-it",
        "openai-community/gpt2-large",
    ]
    model_tokenizer_pairs = load_models(model_ids)

    agents = []
    evaluators = []
    for idx, (model, tokenizer) in enumerate(model_tokenizer_pairs):
        agents.append(LLMAgent(model, tokenizer, name=f"Agent {idx+1}"))
        evaluators.append(EvaluatorAgent(model, tokenizer, name=f"Evaluator {idx+1}"))

    answers = []
    for agent in agents:
        ans = agent.answer(query, use_search=False).split('Answer:')[1].strip()
        answers.append((agent.name, ans))

    all_scores = []
    for idx, evaluator in enumerate(evaluators):
        scores = evaluator.rate_answers(query, [ans[1] for ans in answers], self_idx=idx)
        all_scores.append(scores)

    final_scores = np.mean(np.array(all_scores), axis=0)
    best_idx = int(np.argmax(final_scores))
    
    metrics = pd.DataFrame({
        "Model": model_ids,
        model_ids[0]: all_scores[0],
        model_ids[1]: all_scores[1],
        model_ids[2]: all_scores[2],
        "Mean": final_scores
    })

    return answers, best_idx, final_scores[best_idx], metrics

st.title("LLM Agent Comparison Web App")
query = st.text_input("Enter your question:")

if query:
    answers, best_idx, best_score, metrics = run(query)
    
    st.subheader("Answers")
    for i, (agent_name, ans) in enumerate(answers):
        st.markdown(f"**{agent_name}:** {ans}")

    st.subheader("Best Answer")
    st.markdown(f"**{answers[best_idx][0]}** selected with score **{best_score:.2f}**")
    st.markdown(f"> {answers[best_idx][1]}")

    st.subheader("Evaluation Metrics")
    st.dataframe(metrics)