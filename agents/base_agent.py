from tools.web_search import search_web

class LLMAgent:
    def __init__(self, model, tokenizer, name="Agent"):
        self.model = model
        self.tokenizer = tokenizer
        self.name = name

    def generate(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(**inputs, max_new_tokens=80)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def answer(self, query, use_search=True):
        if use_search:
            search_results = search_web(query)
            context = "\n".join(search_results)
            prompt = f"Use the following information to answer the following question in only 1-2 paragraphs, do not follow up and end the conversation.\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"
        else:
            prompt = f"Answer the following question in only 1-2 paragraphs, do not follow up and end the conversation:\n{query}\nAnswer:"

        return self.generate(prompt)