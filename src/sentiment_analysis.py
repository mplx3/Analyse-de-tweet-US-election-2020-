import pandas as pd

class SentimentAnalysis:
    def __init__(self, model, text_column):
        self.model = model
        self.text_column = text_column

    def analyze_dataframe(self, df):
        results = df[self.text_column].apply(self.model.predict)
        df["sentiment"] = results.apply(lambda x: x[0])
        df["intensity"] = results.apply(lambda x: x[1])
        return df