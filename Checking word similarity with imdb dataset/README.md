# 🔍 Sentiment Classification with Custom and Pretrained Word Embeddings

This project focuses on sentiment classification of movie reviews using both a **custom-trained embedding (E2)** and **Google's pretrained Word2Vec model**. The classification is performed using several deep learning architectures, with special attention to data preprocessing, dimensionality reduction, and performance comparison between models.

---

## 📌 Objectives

- Preprocess IMDB-like textual data and clean it thoroughly.
- Construct a custom word embedding (E2) based on co-occurrence and train it with a simple neural network.
- Apply KMeans clustering for intelligent data reduction.
- Use both **custom embeddings** and **pretrained Word2Vec** embeddings for sentence representation.
- Train and evaluate models: **MLP**, **RNN (LSTM)**, **CNN**, and **Hybrid CNN + LSTM**.
- Compare model performance across embedding strategies and identify the best setup for limited data.

---

## 🧪 Dataset Description

- Source: IMDB-like movie review data.
- Labels: `1` (negative), `2` (positive)
- After preprocessing and filtering rare words, the dataset was reduced to **~300 samples** using clustering and sampling.

---

## ⚙️ Pipeline Summary

### 🔹 Step 1: Preprocessing
- Lowercasing, HTML tag removal, punctuation removal.
- Tokenization and stopword removal using NLTK.
- Rare word filtering (`min_freq=2 or 3`).

### 🔹 Step 2: Dimensionality Reduction & Clustering
- BOW vectors constructed.
- Truncated SVD applied to reduce dimension.
- KMeans clustering (`k=7`) used to group similar samples.
- Data reduction using proportionate sampling from each cluster.

### 🔹 Step 3: Custom Word Embedding (E2)
- Built using one-hot encoding context pairs.
- Trained with a two-layer dense model (output is softmax over vocabulary).
- Final embedding dimension: `100`.

### 🔹 Step 4: Sentence Embeddings
- **E2 Mapping**: average or sequence of custom-trained vectors.
- **Word2Vec Mapping**: pretrained vectors from `gensim` (`Google News 300-dim`).

---

## 🧠 Models

| Model        | Description |
|--------------|-------------|
| `MLP`        | Average word vectors → Dense layers for classification |
| `RNN`        | LSTM over word sequences |
| `CNN`        | 1D Convolution + Global Max Pooling |
| `Hybrid`     | 1D CNN + LSTM combination |

Each model is trained separately on both E2 and Word2Vec sentence representations.

---

## 📊 Results

| Embedding      | MLP     | RNN     | CNN     | Hybrid  |
|----------------|---------|---------|---------|---------|
| **E2 (Custom)**| ~0.76   | ~0.65   | ~0.60   | ~0.67   |
| **Word2Vec**   | ~0.73   | ~0.65   | **0.75**| ~0.66   |

**Conclusion**:
- CNN with Word2Vec performed best for this small dataset.
- MLP is very stable and efficient.
- RNN and Hybrid models are too complex for small data without clear advantage.
- Pretrained embeddings are beneficial in low-data regimes.

---

## 📁 Folder Structure

```
.
├── data/                       # Preprocessed and reduced token data
├── embeddings/                # Custom-trained embedding weights
├── models/                    # Saved Keras models
├── notebooks/                 # Jupyter notebooks with experiments
├── results/                   # Accuracy & loss plots, evaluation reports
└── README.md                  # This file
```

---

## 🧰 Libraries Used

- `nltk`, `sklearn`, `gensim`, `numpy`, `tensorflow.keras`
- Optional: `matplotlib` for visualization

---

## 👨‍💻 Author

Developed by **[Your Name]** as part of an NLP coursework exercise.
