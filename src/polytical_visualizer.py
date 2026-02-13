import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates


plt.rcParams['font.family'] = 'DejaVu Sans'

class PoliticalVisualizer:
    def __init__(self, labeler):
        self.labeler = labeler
        sns.set_theme(style="whitegrid")

    def plot_top_influencers(self, camp, min_tweets=3):
        """Affiche les 10 plus gros influenceurs d'un camp."""
        subset = self.labeler.user_study[
            (self.labeler.user_study['camp'] == camp) &
            (self.labeler.user_study['tweet'] >= min_tweets)
        ]
        top_users = subset.nlargest(10, 'user_followers_count')
       
        if top_users.empty:
            print(f"Aucune donnée pour le camp {camp}")
            return
       
        plt.figure(figsize=(10, 5))
        sns.barplot(data=top_users, y='user_name', x='user_followers_count', hue='user_name', palette='magma', legend=False)
        plt.title(f"Top 10 Influenceurs ({camp})")
        plt.tight_layout()
        plt.show()

    def plot_temporal_volume(self):
        """Volume de tweets avec moyenne mobile 7j."""
        df = self.labeler.df.copy()
       
       
        if 'date' not in df.columns:
           
            for col in ['created_at', 'tweet_created', 'date']:
                if col in df.columns:
                    df['date'] = pd.to_datetime(df[col], errors='coerce')
                    break
       
        df = df.dropna(subset=['date']).set_index('date')
       
        # Agrégation journalière par camp
        daily = df.groupby([pd.Grouper(freq='D'), 'camp']).size().unstack(fill_value=0)
       
        if not daily.empty:
            daily.rolling(7, min_periods=1).mean().plot(figsize=(12, 4))
            plt.title('Volume de tweets (moyenne mobile 7j) par camp')
            plt.ylabel('Nombre de tweets')
            plt.tight_layout()
            plt.show()

    def plot_source_distribution(self):
        """Répartition des sources (iPhone, Web, etc.) par camp."""
        df = self.labeler.df
       
        if 'source' not in df.columns:
            print("Erreur : La colonne 'source' est absente du dataset.")
            return

        # On prend les 3 sources les plus fréquentes
        top_sources = df['source'].value_counts().nlargest(3).index
        df_sub = df[df['source'].isin(top_sources)]
       
        plt.figure(figsize=(10, 6))
        sns.countplot(data=df_sub, x='source', hue='camp', palette='muted')
        plt.title("Répartition des terminaux par camp politique")
        plt.ylabel("Nombre de Tweets")
        plt.tight_layout()
        plt.show()