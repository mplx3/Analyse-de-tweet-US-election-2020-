import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Visualizer:
    def plot_sentiment_proportions(self, df_trump, df_biden, output_path):
        df_trump["candidate"] = "Trump"
        df_biden["candidate"] = "Biden"
        combined = pd.concat([df_trump, df_biden])

        plt.figure(figsize=(16, 6))
        plt.subplot(1, 2, 1)

        sns.barplot(
            data=combined,
            x="sentiment",
            y="intensity",
            hue="candidate",
            estimator=lambda x: len(x) / len(combined) * 200,
            palette={"Trump": "red", "Biden": "blue"}
        )

        plt.title("Proportion des sentiments (utilisateurs uniques)")
        plt.ylabel("Pourcentage (%)")

        # Intensité émotionnelle
        plt.subplot(1, 2, 2)

        for label, df in [("Trump", df_trump), ("Biden", df_biden)]:
            neg = df[df["sentiment"] == "negative"]["intensity"]
            pos = df[df["sentiment"] == "positive"]["intensity"]

            sns.kdeplot(neg, label=f"{label} négatif", fill=True)
            sns.kdeplot(pos, label=f"{label} positif", fill=True)

        plt.title("Intensité émotionnelle (positive vs négative)")
        plt.xlabel("Score d’intensité")
        plt.legend()

        plt.tight_layout()
        plt.savefig(output_path)