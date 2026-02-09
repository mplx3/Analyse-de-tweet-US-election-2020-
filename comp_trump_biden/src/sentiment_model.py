# src/sentiment_model.py

from transformers import pipeline

class SentimentModel:
    def __init__(self, model_id):
        self.pipeline = pipeline(
            "sentiment-analysis",
            model=model_id,
            tokenizer=model_id,
            device=-1
        )

    def predict(self, text):
        try:
            res = self.pipeline(str(text)[:512])[0]
            return res["label"], res["score"]
        except:
            return "neutral", 0.0
