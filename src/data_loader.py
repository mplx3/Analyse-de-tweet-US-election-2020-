import pandas as pd

class DataLoader:
    def __init__(self, path, user_id_col):
        self.path = path
        self.user_id_col = user_id_col

    def load_unique_users(self, n_samples):
        df = pd.read_csv(self.path, sep=None, engine="python")
        df = df.drop_duplicates(subset=[self.user_id_col])
        return df.sample(min(n_samples, len(df))).copy()
   