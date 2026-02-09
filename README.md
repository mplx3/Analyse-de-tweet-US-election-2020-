# Trump vs Biden – Sentiment Comparison Analysis

##  Project Summary

This project performs a **comparative analysis of Twitter sentiment** regarding **Donald Trump** and **Joe Biden** during the 2020 US Presidential Election. 

The objective is to move beyond simple tweet counts and understand the nuances of public opinion by:
- Comparing the **distribution of sentiments** (positive, neutral, negative).
- Analyzing the **emotional intensity** of tweets using model confidence scores.
- Reducing bias by filtering for **unique users** (one tweet per user).
- Highlighting key differences in public perception between the two candidates.

---

##  Features

* **Transformer-based Analysis:** Powered by state-of-the-art Hugging Face models.
* **User-Centric Filtering:** Eliminates bot/spam bias by retaining only one unique tweet per user.
* **Emotional Intensity Metric:** Uses the model's confidence score to quantify the strength of the sentiment.
* **Data Visualization:** Automated generation of comparative charts for quick interpretation.
* **Modular Architecture:** Clean, OOP-based Python structure.

---

##  Models & Methodology

### Model Specifications
- **Model:** `cardiffnlp/twitter-roberta-base-sentiment-latest`
- **Architecture:** RoBERTa (Transformer)
- **Training Data:** Twitter-specific corpus (optimized for slang and social media syntax).
- **Inference Only:** No fine-tuning required; the model is used in its pre-trained state for maximum reliability on generic Twitter data.

### Process Flow
1. **Data Cleaning:** Tweets are grouped by candidate and filtered by `user_id`.
2. **Inference:** Each unique tweet is passed through the RoBERTa pipeline.
3. **Metrics Calculation:** - **Labels:** Negative, Neutral, Positive.
    - **Intensity:** The probability score of the predicted label.
4. **Comparison:** Statistical comparison of sentiment ratios between the two datasets.

---

##  Installation Guide

### 1. Clone the repository
```bash
git clone [https://github.com/mplx3/Analyse-de-tweet-US-election-2020-.git](https://github.com/mplx3/Analyse-de-tweet-US-election-2020-.git)
cd Analyse-de-tweet-US-election-2020-
````
### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Project Structure
```bash
comp_trump_biden/
│
├── data/
│   ├── trump_nort.csv
│   ├── biden_nort.csv
│
├── src/
│   ├── data_loader.py
│   ├── sentiment_analyzer.py
│   ├── comparator.py
│   ├── visualizer.py
|   ├── main.py
│
├── results/
│   └── comparison_trump_biden.png
│
├── requirements.txt
└── README.md
```

## How to Run
Execute the analysis from the root directory:
```bash
python src/main.py
```

## Visualizations & Results
All generated figures are saved in the results/ folder. Key outputs include:
Sentiment Distribution: A bar chart comparing the percentage of positive, neutral, and negative feelings for each candidate.
Emotional Intensity: A comparison of how strongly (confidence) sentiments are expressed.
Example Visualization:

<img width="828" height="601" alt="image" src="https://github.com/user-attachments/assets/b8b32b01-c55a-42cc-ae0d-98de3760f8ce" />

<img width="794" height="570" alt="image" src="https://github.com/user-attachments/assets/d816371f-dd74-4ee6-bce7-1bfdd3a17a48" />
