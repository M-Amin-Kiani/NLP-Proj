# Natural Language Processing - Word Embeddings & Text Classification

> Course Project - Natural Language Processing (NLP)

This project demonstrates how distributed word representations (Word Embeddings) can be used for document representation and text classification. Two different embedding approaches are investigated and compared:

- Training **Word2Vec** embeddings from scratch.
- Using **pre-trained GloVe** embeddings.

The generated document embeddings are then evaluated using several classical machine learning classifiers for sentiment analysis and topic classification.
<img width="358" height="213" alt="image" src="https://github.com/user-attachments/assets/bd628546-89f8-4229-a039-634462e6baa8" />

---

# Project Objectives

The main objectives of this project are:

- Learn how Word Embeddings represent semantic information.
- Train a Word2Vec model on a custom corpus.
- Use pre-trained GloVe vectors.
- Build document embeddings by averaging word vectors.
- Compare different embedding dimensions.
- Evaluate multiple classification algorithms.
- Analyze Out-of-Vocabulary (OOV) words.
- Compare training embeddings from scratch versus using pre-trained embeddings.

---

# Datasets

## 1. NLTK Movie Reviews

Binary sentiment classification.

Classes:

- Positive
- Negative

Number of documents:

- 2000 movie reviews

---

## 2. BBC News Dataset

Multi-class news classification.

Classes:

- Business
- Entertainment
- Politics
- Sport
- Technology

Number of documents:

- 2225 news articles

---

# Word Embedding Models

## Word2Vec

Word2Vec is trained **from scratch** using only the Movie Reviews training set.

The following embedding dimensions are evaluated:

- 50
- 100
- 200

Training parameters:

| Parameter    |     Value |
| ------------ | --------: |
| Architecture | Skip-Gram |
| Window       |         5 |
| Min Count    |         2 |
| Epochs       |        10 |

---

## GloVe

Instead of training embeddings, this project also evaluates the widely-used **pre-trained GloVe 6B** vectors.

Embedding dimensions:

- 50
- 100
- 200
- 300

The project also computes the Out-of-Vocabulary (OOV) percentage for every experiment.

---

# Document Representation

Individual word vectors cannot directly classify an entire document.

Therefore each document is represented as the **average of all word vectors** contained in that document.

If a word does not exist inside the embedding vocabulary, it is ignored.

If a document contains no known words, a zero vector is returned.

---

# Classification Models

The following classifiers are evaluated.

- Logistic Regression
- Linear Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)

Optional experiments include:

- Decision Tree
- Random Forest
- Gaussian Naive Bayes
- XGBoost

---

# Project Structure

```
.
├── code
│   ├── exercise2.py
│   ├── bbc/
│   ├── glove/
│   └── outputs/
│
├── report
│   └── NLP_Report.pdf
│
└── README.md
```

---

# Installation

Install the required Python packages:

```bash
pip install numpy
pip install pandas
pip install nltk
pip install gensim
pip install scikit-learn
pip install matplotlib
pip install xgboost
```

---

# Download Required Datasets

BBC Dataset

http://mlg.ucd.ie/files/datasets/bbc-fulltext.zip

GloVe Embeddings

https://nlp.stanford.edu/data/glove.6B.zip

Extract both folders inside the project directory.

---

# Running the Project

Simply execute

```bash
python exercise2.py
```

or run the notebook inside Jupyter Notebook / VS Code.

---

# Evaluation Metrics

The project evaluates every classifier using

- Accuracy
- Precision
- Recall
- F1-score
- Macro F1
- Confusion Matrix

For the BBC dataset the OOV percentage is also reported.

---

# Optional Experiment

An additional experiment is implemented to reduce the Out-of-Vocabulary rate.

The procedure is:

1. Train a Word2Vec model on the BBC corpus.
2. Extract vectors for previously unseen words.
3. Extend the original GloVe vocabulary.
4. Recompute document embeddings.
5. Compare classification performance before and after vocabulary expansion.

---

# Results

The project compares:

- Different embedding dimensions
- Word2Vec vs GloVe
- Binary vs Multi-class classification
- Multiple classifiers
- OOV before and after vocabulary expansion

The generated confusion matrices help identify which classes are most frequently confused.

---

# Key Concepts Covered

- Natural Language Processing
- Word Embeddings
- Word2Vec
- GloVe
- Skip-Gram
- Semantic Representation
- Document Embedding
- Out-of-Vocabulary (OOV)
- Binary Classification
- Multi-class Classification
- Logistic Regression
- Linear SVM
- KNN
- Random Forest
- XGBoost

---

# References

- Tomas Mikolov et al. (2013). Efficient Estimation of Word Representations in Vector Space.
- Jeffrey Pennington et al. (2014). GloVe: Global Vectors for Word Representation.
- NLTK Documentation
- Gensim Documentation
- Scikit-learn Documentation

---

# License

This repository is intended for educational and research purposes.
