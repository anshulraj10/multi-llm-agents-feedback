from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from huggingface_hub import login
import os
from dotenv import load_dotenv

def load_models(model_ids):
    load_dotenv()
    token = os.getenv("HF_ACCESS_TOKEN")
    login(token=token)
    
    models = []
    for model_id in model_ids:
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForCausalLM.from_pretrained(model_id, device_map="mps", torch_dtype=torch.float16)
        models.append((model, tokenizer))
    return models