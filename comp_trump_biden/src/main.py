# main.py

from config import MODEL_ID, N_TWEETS, TEXT_COLUMN, USER_ID_COLUMN
from data_loader import DataLoader
from sentiment_model import SentimentModel
from sentiment_analysis import SentimentAnalysis
from visualization import Visualizer




print("--- Chargement des données ---")

loader_trump = DataLoader("data/trump_nort.csv", USER_ID_COLUMN)
loader_biden = DataLoader("data/biden_nort.csv", USER_ID_COLUMN)

df_trump = loader_trump.load_unique_users(N_TWEETS)
df_biden = loader_biden.load_unique_users(N_TWEETS)

print(f"Analyse basée sur {len(df_trump)} utilisateurs Trump et {len(df_biden)} Biden")

print("--- Initialisation du modèle de sentiment ---")
model = SentimentModel(MODEL_ID)
analysis = SentimentAnalysis(model, TEXT_COLUMN)

print("--- Analyse de sentiment ---")
df_trump = analysis.analyze_dataframe(df_trump)
df_biden = analysis.analyze_dataframe(df_biden)

print("--- Visualisation ---")
viz = Visualizer()
viz.plot_sentiment_proportions(
    df_trump,
    df_biden,
    "results/comparaison_utilisateurs_uniques.png"
)

print("✅ Analyse Trump vs Biden terminée")
