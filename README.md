Analyse de l'Alignement Politique sur Twitter ⚖️
Ce projet est une application Python conçue pour analyser le sentiment et l'alignement politique de tweets concernant les candidats à l'élection (Trump vs Biden). Il transforme des données brutes en insights visuels, identifiant les influenceurs clés et les tendances temporelles par camp politique.

📁 Structure du Projet
L'application est découpée en trois modules principaux pour garantir une maintenance facile et une séparation des responsabilités :

main.py : Le point d'entrée du programme. Il orchestre le chargement des données, le traitement et la génération des graphiques.

PoliticalLabeler.py : La classe "moteur". Elle calcule les scores d'alignement basés sur le sentiment et le candidat, agrège les données par utilisateur et définit les seuils des camps (Biden, Trump, Neutre).

PoliticalVisualizer.py : La classe de visualisation. Elle utilise Seaborn et Matplotlib pour générer des analyses graphiques (Top influenceurs, volume temporel, sources des terminaux).

🚀 Installation
Prérequis : Assurez-vous d'avoir Python 3.11+ installé.

Bibliothèques nécessaires :

Bash
pip install pandas numpy matplotlib seaborn
Données : Placez votre fichier tweets_with_sentiment.csv dans un dossier nommé Data/ à la racine du projet.

🛠️ Utilisation
Pour lancer l'analyse complète, exécutez simplement le script principal :

Bash
python main.py
Logique d'Alignement
Le score d'alignement est calculé selon la règle suivante :

Pro-Trump : Sentiment positif sur Trump OU sentiment négatif sur Biden.

Pro-Biden : Sentiment positif sur Biden OU sentiment négatif sur Trump.

Neutre : Tout tweet marqué comme 'neutral'.

📊 Fonctionnalités de Visualisation
Le projet génère automatiquement plusieurs types de graphiques :

Top 10 Influenceurs : Identifie les comptes ayant le plus de followers pour chaque camp.

Analyse Temporelle : Affiche le volume de tweets par camp avec une moyenne mobile sur 7 jours pour lisser les tendances.

Répartition des Sources : Compare les terminaux utilisés (iPhone, Android, Web) selon l'appartenance politique.

⚖️ Gestion des Camps
Les utilisateurs sont segmentés selon la distribution statistique (quantiles) de leurs scores moyens :

Camp Biden : 40% inférieurs des scores.

Camp Neutre : 20% centraux.

Camp Trump : 20% supérieurs (Top 80% percentile).
