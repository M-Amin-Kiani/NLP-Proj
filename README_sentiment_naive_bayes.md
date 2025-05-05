
# 🎬 Sentiment Analysis with Manual Naive Bayes (from Scratch)

This project implements a **fully manual Naive Bayes classifier** to perform **sentiment analysis** on the [NLTK movie_reviews dataset](https://www.nltk.org/howto/corpus.html). No prebuilt classifiers are used — everything is coded from scratch, including tokenization, vocabulary building, and probability computation.

---

## 📌 What is This?

A simple yet powerful sentiment classification pipeline written in pure Python + NLTK that:
- Classifies movie reviews as **positive** or **negative**
- Uses **manual probability computation** (not `NaiveBayesClassifier`)
- Evaluates with real metrics like **Accuracy**, **Precision**, **Recall**, and **F1-Score**
- Preprocesses the text completely (cleaning, filtering, normalization)
- Shows **most informative features** that drive the predictions

---

## ⚙️ Pipeline Overview

1. **Data Loading**  
   Uses `movie_reviews` corpus from NLTK (2000 reviews, balanced pos/neg).

2. **Preprocessing**  
   - Lowercasing
   - Removing:
     - Punctuation
     - Stopwords
     - Numbers
     - URLs
     - Very short/meaningless words
     - Custom non-informative tokens (`just`, `even`, etc.)

3. **Vocabulary Filtering**
   - Removes words with frequency < 3
   - Keeps only top 4000 most frequent words

4. **Training (Manual Naive Bayes)**
   - Count-based word statistics per class
   - Uses **log-count smoothing**
   - Applies **class prior bias** to improve recall

5. **Evaluation**
   - Metrics: Accuracy, Precision, Recall, F1 (for each class)
   - Tested on 20% of the dataset
   - Balanced and interpretable results

---

## 💡 Key Features

✅ 100% manual Naive Bayes — no scikit-learn  
✅ End-to-end preprocessing pipeline  
✅ Feature filtering & token weighting  
✅ Realistic NLP task with solid results  
✅ Interpretable model behavior (shows key words like `seagal`, `outstanding`, etc.)

---

## 📈 Sample Output

```
Accuracy: 82.5%

              precision    recall  f1-score   support

         neg     0.8249    0.8221    0.8235       298
         pos     0.8251    0.8278    0.8264       302

    accuracy                         0.8250       600
   macro avg     0.8250    0.8250    0.8250       600
weighted avg     0.8250    0.8250    0.8250       600
```

---

## 🚀 How to Run

1. Install required libraries:

```bash
pip install nltk scikit-learn
```

2. Run the script in Jupyter/Colab or local Python:

```python
# Download corpus (first run only)
import nltk
nltk.download('movie_reviews')
nltk.download('punkt')
nltk.download('stopwords')
```

3. Execute the script.

---

## 🧪 To Do / Ideas

- Add visualization for word frequencies
- Add confusion matrix plotting
- Add TF-IDF support (still manually)
- Extend to multiclass sentiment

---

## 📁 Files

- `naive_bayes_sentiment.py` → Full code
- `README.md` → This file
- `output.txt` (optional) → Sample metrics

---

## 📜 License

MIT License © 2025

---

## ✍️ Author

Built with ❤️ by [Your Name] as part of a university NLP assignment.
