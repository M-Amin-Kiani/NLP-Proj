# 🎼 N-Gram Music Language Model

A complete statistical music language modeling project based on **N-gram Language Models** and **Lidstone Smoothing** for predicting and generating musical note sequences.

This project was developed as part of an NLP / Statistical Language Modeling assignment and demonstrates how classic NLP techniques can be applied to symbolic music generation.
<img width="434" height="237" alt="image" src="https://github.com/user-attachments/assets/c6c05771-3657-4e5f-958f-7b0f815ae964" />

---

# 📌 Project Overview

In this project, we build a simple statistical language model that learns patterns from musical note sequences and predicts the continuation of incomplete melodies.

The system:

- Reads a dataset of musical note sequences
- Trains:
  - Unigram models
  - Bigram models
  - Trigram models
- Applies:
  - Laplace smoothing
  - Lidstone smoothing
- Tunes smoothing hyperparameters using validation perplexity
- Generates note completions for incomplete musical prompts
- Evaluates models using perplexity
- Experiments with:
  - Removing modifiers (`b`, `k`)
  - Conditioning on `dastgah`

---

# 🧠 Main Concepts Used

This project covers important NLP and probabilistic modeling concepts:

| Concept                | Description                              |
| ---------------------- | ---------------------------------------- |
| N-gram Language Models | Predict next token using previous tokens |
| Unigram                | Uses no context                          |
| Bigram                 | Uses previous 1 note                     |
| Trigram                | Uses previous 2 notes                    |
| Lidstone Smoothing     | Prevents zero probabilities              |
| Laplace Smoothing      | Special case of Lidstone where α = 1     |
| Perplexity             | Measures model uncertainty               |
| Vocabulary Size        | Number of unique note tokens             |
| Data Sparsity          | Problem of rare/unseen note combinations |

---

# 🎵 Dataset Structure

The dataset (`music.csv`) contains:

| Column    | Description            |
| --------- | ---------------------- |
| `name`    | Piece name             |
| `note`    | Musical note sequence  |
| `dastgah` | Musical mode / dastgah |

Example:

```csv
name,note,dastgah
piece1,C D E F G,Shur
piece2,A Bb C D,Mahur
```

---

# ⚙️ Project Features

## ✅ 1. Note Normalization

The model supports two modes:

### A) Keep modifiers

Examples:

```text
Bb ≠ B
Db ≠ D
Ab ≠ A
```

### B) Ignore modifiers

Examples:

```text
Bb → B
Db → D
Ab → A
```

This reduces vocabulary size and sparsity.

---

## ✅ 2. Multiple N-gram Models

The project trains:

- Unigram
- Bigram
- Trigram

Each model learns transition probabilities between notes.

---

## ✅ 3. Lidstone Smoothing

We use Lidstone smoothing:

\[
P(w|h)=\frac{C(h,w)+\alpha}{C(h)+\alpha V}
\]

Where:

| Symbol     | Meaning             |
| ---------- | ------------------- |
| \(C(h,w)\) | Count of n-gram     |
| \(C(h)\)   | Count of context    |
| \(V\)      | Vocabulary size     |
| \(\alpha\) | Smoothing parameter |

Special cases:

| α   | Method            |
| --- | ----------------- |
| 1   | Laplace smoothing |
| 0.5 | Jeffreys-Perks    |
| 0   | No smoothing      |

---

## ✅ 4. Hyperparameter Tuning

The project automatically selects the best α using:

- Leave-One-Out Validation
- Validation Perplexity

Tested values:

```python
ALPHA_GRID = [0.1, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0, 1.5, 2.0]
```

---

## ✅ 5. Perplexity Evaluation

Perplexity measures how uncertain the model is.

Lower perplexity = better predictions.

\[
PP(W)=\exp\left(-\frac{1}{N}\sum \log P(w_i)\right)
\]

---

## ✅ 6. Music Generation

The trained model generates note completions using:

- Greedy decoding
- Beam Search generation

for incomplete prompts such as:

```text
S S S S
G C G C
A Bb C D
```

---

# 📂 Project Structure

```text
project/
│
├── music.csv
├── music_ngram.py
├── README.md
└── results/
```

---

# 🚀 Installation

## Clone repository

```bash
git clone https://github.com/yourusername/ngram-music-lm.git
cd ngram-music-lm
```

---

## Install dependencies

```bash
pip install pandas numpy
```

---

# ▶️ Running the Project

## Run normally

```bash
python music_ngram.py
```

---

# 📊 Example Output

```text
[n=2] best alpha = 1.0
validation perplexity = 9.1658
train perplexity = 7.5064
```

Meaning:

| Output                | Meaning                    |
| --------------------- | -------------------------- |
| `n=2`                 | Bigram model               |
| `alpha=1.0`           | Laplace smoothing          |
| Validation perplexity | Generalization performance |
| Train perplexity      | Training-set uncertainty   |

---

# 🧩 Understanding Vocabulary Size

Vocabulary Size = Number of unique note tokens.

Examples:

| Mode                       | Vocabulary |
| -------------------------- | ---------- |
| Keep modifiers             | 14         |
| Ignore modifiers           | 8          |
| Ignore modifiers + dastgah | 13         |
| Keep modifiers + dastgah   | 19         |

---

# 🎯 Why Modifier Removal Helps

Ignoring modifiers:

- Reduces vocabulary size
- Reduces sparsity
- Improves statistical learning
- Improves perplexity

BUT:

- Removes musical detail
- Loses distinction between notes

Example:

```text
Bb and B become identical
```

This creates a trade-off between:

```text
Statistical simplicity vs Musical precision
```

---

# 📈 Experimental Findings

## Best overall model

In most experiments:

- Bigram models generalized best
- Trigram models overfitted slightly
- Unigram models lacked contextual understanding

---

## Best smoothing

Observed behavior:

| Model   | Best α    |
| ------- | --------- |
| Unigram | Larger α  |
| Bigram  | Medium α  |
| Trigram | Smaller α |

Reason:

Higher-order models become sparse faster and need careful smoothing.

---

# 🔍 Why Some Notes Rarely Appear

Rare notes such as:

```text
Ab
Db
Eb
```

appear less because:

- Dataset is small
- Some notes are naturally infrequent
- Beam search prefers high-probability notes
- Common transitions dominate generation

---

# 🧠 Key NLP Insights Learned

This project demonstrates several core NLP principles:

## 1. Context matters

Bigram/trigram outperform unigram because previous notes help prediction.

---

## 2. Sparsity is critical

Higher-order n-grams suffer from unseen combinations.

---

## 3. Smoothing is essential

Without smoothing:

```text
Unseen n-grams → probability = 0
```

which breaks generation and perplexity calculations.

---

## 4. Smaller vocabulary often improves statistical performance

But may reduce semantic/musical richness.

---

# 📚 Mathematical Background

## N-gram Probability

### Unigram

\[
P(w_i)
\]

### Bigram

\[
P(w*i|w*{i-1})
\]

### Trigram

\[
P(w*i|w*{i-2},w\_{i-1})
\]

---

# 🛠 Future Improvements

Possible extensions:

- Kneser-Ney smoothing
- Interpolated n-grams
- Neural language models
- LSTM / GRU generation
- Transformer-based music generation
- Temperature sampling
- MIDI export support

---

# 📖 Educational Value

This project is highly useful for understanding:

- Statistical NLP
- Sequence modeling
- Probability estimation
- Smoothing methods
- Generative models
- Music informatics

---

# 👨‍💻 Author

Developed for an NLP / Language Modeling assignment.

---

# 📜 License

UI License
