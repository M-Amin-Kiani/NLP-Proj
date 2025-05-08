# 🧠 Persian Word Embedding with Naab Corpus | GloVe + Word2Vec + FastText

A complete NLP pipeline for training and comparing Persian word embeddings on the [Naab](https://huggingface.co/datasets/SLPL/naab) corpus.  
This project is developed as part of a university-level NLP coursework, implementing **from-scratch**, **fast** and **scalable** vector space models on large Persian text data.

---

## 📦 Dataset

- **Naab Corpus**: A massive Persian language dataset available at:
  → https://huggingface.co/datasets/SLPL/naab
- We use only **10% of the corpus**, streamed and saved via HuggingFace Datasets API.

---

## 🔧 Preprocessing

Performed using:
- `nltk` for Persian stopword removal and tokenization
- Minimal regex-based cleaner
- Preprocessed texts tokenized to `sentences: List[List[str]]`

---

## 📌 Models Implemented

### 1. Word2Vec (Skip-Gram)
- Trained using a custom Keras-based neural network
- Uses `(center, context)` skip-gram pairs
- Works on 100,000+ tokenized sentences

### 2. FastText (Subword-aware)
- Trained using the official Facebook `fasttext` Python package
- Generates `.bin` and `.vec` files (optional)
- Learns from character n-grams (handles rare & OOV words)

### 3. GloVe (From Scratch)
- Fully manual NumPy-based implementation following:
  → **GloVe: Global Vectors for Word Representation**  
  → Pennington et al., [Stanford NLP](https://arxiv.org/abs/1406.2038)
- Built on co-occurrence matrix
- Loss function: Weighted least squares with log(Xij)
- Custom gradient descent loop

---

## 📊 Visualization

- PCA and t-SNE plots to visualize 2D projections of embeddings
- matplotlib used for clear labeling
- Comparison between Word2Vec, FastText, and GloVe

---

## 🔍 Semantic Similarity Analysis

Evaluated similarity for multiple Persian anchor words:

| Anchor Word | Top Similar (W2V) | Top Similar (FastText) |
|-------------|-------------------|-------------------------|
| کتاب        | فروش، دانشجو ... | کتابی، جلد، مجلد ...   |
| دانشگاه     | پژوهش، استاد ... | دانشگاها، آموزش، پژوهش |
| زن          | دختر، مادر ...   | زنان، زنش، همسر ...    |

---

## 📑 Comparison

| Feature           | Word2Vec      | FastText       | GloVe (Scratch) |
|------------------|---------------|----------------|-----------------|
| OOV handling     | ❌ No         | ✅ Yes         | ❌ No           |
| Subword learning | ❌            | ✅             | ❌              |
| Requires corpus? | ✅            | ✅             | ✅              |
| Uses co-matrix   | ❌            | ❌             | ✅              |
| Speed            | ⚡ Fast       | ⚡⚡ Faster     | 🐢 Slower       |

---

## 🧾 References

- [GloVe Paper (Stanford NLP)](https://arxiv.org/abs/1406.2038)
- [Word2Vec Skip-Gram Paper (Mikolov et al.)](https://arxiv.org/abs/1301.3781)
- [FastText by Facebook Research](https://arxiv.org/abs/1607.04606)
- [Naab Dataset](https://huggingface.co/datasets/SLPL/naab)
- [Vec2Word Paper (2022)](https://arxiv.org/abs/2208.13486)

---

## 🖥 Run on Colab

Compatible with:
- CPU, GPU, TPU (`v2-8` runtime in Colab)
- Includes TPU fallback if unavailable

---

## 📁 Project Structure

```
├── glove_from_scratch.py
├── glove_analysis_compare.py
├── fasttext_training.py
├── word2vec_skipgram.py
├── compare_word2vec_fasttext.py
├── naab_streamed_10percent.jsonl
└── visualizations/
    ├── pca.png
    └── tsne.png
```

---

## 🔐 License

MIT License – For educational & research use.