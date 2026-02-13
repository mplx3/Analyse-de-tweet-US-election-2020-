import pandas as pd
import os
import warnings
# Ignore les avertissements de police dans la console
warnings.filterwarnings("ignore", category=UserWarning)

from PoliticalLabeler import PoliticalLabeler
from PoliticalVisualizer import PoliticalVisualizer

# 1. Chargement robuste des données
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'Data', 'tweets_with_sentiment.csv')

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    # Chemin alternatif si lancé depuis un dossier différent
    df = pd.read_csv('Data/tweets_with_sentiment.csv')

# 2. Lancement du moteur
engine = PoliticalLabeler(df)
engine.compute_alignment_scores().aggregate_users().define_camps()

# 3. Création des visuels
viz = PoliticalVisualizer(engine)

print("--- Affichage : Biden ---")
viz.plot_top_influencers('Biden')

print("--- Affichage : Trump ---")
viz.plot_top_influencers('Trump')

print("--- Affichage : Temporel & Sources ---")
viz.plot_temporal_volume()
viz.plot_source_distribution()

# 4. Résumé final
print(f"\nAnalyse terminée.")
print(f"Seuil Biden : {engine.thresholds['low']:.4f}")
print(f"Seuil Trump : {engine.thresholds['high']:.4f}")