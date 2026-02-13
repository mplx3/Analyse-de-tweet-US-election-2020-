from transformers import pipeline

class SentimentModel:
    def __init__(self, model_id,n_device):
        self.pipeline = pipeline(
            "sentiment-analysis",
            model=model_id,
            tokenizer=model_id,
            device=n_device
        )

    def predict(self, text):
        try:
            res = self.pipeline(str(text)[:512])[0]
            return res["label"], res["score"]
        except:
            return "neutral", 0.0