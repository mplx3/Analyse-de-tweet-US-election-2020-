import pandas as pd
import numpy as np
import re
from collections import Counter

class PoliticalLabeler:
    def __init__(self, df):
        self.df = df.copy()
        self.user_study = None
        self.thresholds = {}

    def compute_alignment_scores(self):
        """Calcule le score d'alignement pour chaque tweet."""
        def _logic(row):
            s = row.get('score', 0)
            sent = str(row.get('sentiment', '')).lower()
            cand = str(row.get('candidate', '')).lower()
           
            if sent == 'neutral': return 0.0
           
            # Pro-Trump: Trump+/Biden- | Pro-Biden: Biden+/Trump-
            if cand == 'trump':
                return s if sent == 'positive' else -s
            elif cand == 'biden':
                return -s if sent == 'positive' else s
            return 0.0

        self.df['alignment_score'] = self.df.apply(_logic, axis=1)
        return self

    def aggregate_users(self):
        """Groupe les données par utilisateur."""
        self.user_study = self.df.groupby('user_id').agg({
            'user_name': 'first',
            'user_followers_count': 'max',
            'likes': 'sum',
            'retweet_count': 'sum',
            'tweet': 'count',
            'alignment_score': 'mean',
            'tweet_original': lambda x: ' '.join(str(v) for v in x)
        }).reset_index()
       
        # Calcul de la stabilité (écart-type)
        stability = self.df.groupby('user_id')['alignment_score'].std().reset_index(name='stability')
        self.user_study = self.user_study.merge(stability, on='user_id')
        return self

    def define_camps(self, low_q=0.40, high_q=0.80):
        """Attribue un camp (Biden/Trump/Neutral) selon les quantiles."""
        l_q = self.user_study['alignment_score'].quantile(low_q)
        h_q = self.user_study['alignment_score'].quantile(high_q)
        self.thresholds = {'low': l_q, 'high': h_q}

        def _label(val):
            if val <= l_q: return 'Biden'
            if val >= h_q: return 'Trump'
            return 'Neutral'

        self.user_study['camp'] = self.user_study['alignment_score'].apply(_label)
        # Reporter le camp sur le dataframe principal pour l'analyse temporelle
        self.df = self.df.merge(self.user_study[['user_id', 'camp']], on='user_id', how='left')
        return self

    @staticmethod
    def get_top_hashtags(text_series, top_n=10):
        all_tags = []
        for t in text_series:
            all_tags += re.findall(r'#(\w+)', str(t).lower())
        return Counter(all_tags).most_common(top_n)