# 🎯 YouTube Spam Detection (NLP Project)

A complete and **leakage-free** Natural Language Processing pipeline for detecting spam comments using classical machine learning techniques.

---

## 🚀 Project Overview

This project classifies YouTube comments into:

- ❌ Spam (1)
- ✅ Not Spam (0)

It focuses on:
- Task-specific preprocessing
- Minimal but effective transformations
- Correct evaluation without data leakage

---

## ⚠️ Data Leakage Prevention

✔ Train/Test split is done BEFORE preprocessing  
✔ Vocabulary is built ONLY on training data  
✔ Vectorizer is fit on train, applied to test  
✔ Spell correction is built only from train  

This ensures valid and realistic results.

---

## 🧠 Preprocessing Strategy

- Lowercasing text
- Replacing:
  - URLs → url
  - Emails → email
  - Mentions → user
- Normalizing repeated characters (e.g., coooool → cool)
- Keeping punctuation signals (! → exclam, ? → quest)
- Optional stopword removal (tested both cases)

---

## 🔹 NLP Variants

- BASE → Basic cleaning
- STEM → Porter stemming
- LEMMA → Lemmatization
- SPELL → Spell correction (train-based)

---

## 🔹 Feature Engineering

- Binary Bag-of-Words
- Unigrams + Bigrams (ngram_range=(1,2))

This helps capture patterns like:
- "check out"
- "subscribe now"
- "visit my channel"

---

## 🤖 Models Used

- KNN
- BernoulliNB
- MultinomialNB
- Logistic Regression
- Linear SVM
- Random Forest

---

## 📊 Best Result

- Model: Logistic Regression
- Preprocessing: STEM
- Stopwords: KEPT
- Accuracy: 96.59%
- F1 Score: 96.47%

---

## 📈 Sample Classification Report

precision    recall  f1-score   support

0     0.9362    1.0000    0.9670
1     1.0000    0.9318    0.9647

Accuracy: 0.9659

---

## 💡 Key Insights

- Stopwords can HELP in spam detection
- Bigrams significantly improve performance
- Logistic Regression works very well on text data
- Simple, task-aware preprocessing beats heavy generic preprocessing
- KNN performs weaker on sparse text data

---

## ▶️ How to Run

Install dependencies:
pip install -r requirements.txt

Run script or notebook:
python your_script.py

---

## 📦 Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn
- nltk

---

## 🔬 Future Work

- Cross-validation
- Deep learning models (BERT, LSTM)
- Better spell correction
- Larger dataset

---

## ⭐ Final Note

Correct methodology + smart preprocessing = strong performance.

---

## 📌 License

Educational use only.
