class EvaluatorAgent:
    def __init__(self, model, tokenizer, name="Evaluator"):
        self.model = model
        self.tokenizer = tokenizer
        self.name = name

    def rate_answers(self, question, all_answers, self_idx):
        scores = []
        for idx, ans in enumerate(all_answers):
            # if idx == self_idx:
            #     scores.append(0.0)  # Do not evaluate self
            #     continue

            eval_prompt = f"Question: {question}\n\nAnswer: {ans}\n\nOn a scale of 0 to 1, how good is this answer based on correctness, completeness, and clarity. Provide only a numeric score. Score:"

            inputs = self.tokenizer(eval_prompt, return_tensors="pt").to(self.model.device)
            outputs = self.model.generate(**inputs, max_new_tokens=50)
            result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            print(result)
            result = result.split("Score:")[1].strip().split()[0]

            # Attempt to extract a float score
            try:
                score = float(result.strip())
                score = max(0.0, min(1.0, score))  # Clamp between 0 and 1
            except:
                score = 0.0
            scores.append(score)

        return scores