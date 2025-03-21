# 📚 WordCloud Generator for Farsi & English Texts with NLP Preprocessing

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat&logo=python" />
  <img src="https://img.shields.io/badge/NLP-Hazm|NLTK-green?style=flat&logo=github" />
  <img src="https://img.shields.io/badge/WordCloud-Visualization-orange?style=flat&logo=plotly" />
</div>

---

## 🧠 About the Project

This project provides a complete and clean pipeline to **preprocess Persian and English texts** and generate **WordClouds** based on the most frequent words.  
It includes proper **text cleaning, tokenization, normalization, lemmatization**, and visual representation of words in the form of **WordClouds**.

---

## 🗂️ Features
- ✅ **Supports both Farsi and English** texts.
- ✅ Uses **Hazm** for Persian NLP tasks.
- ✅ Uses **NLTK** for English NLP tasks.
- ✅ **Follows strict preprocessing steps** according to academic or NLP project needs.
- ✅ Saves cleaned text to separate `.txt` files.
- ✅ Generates WordClouds with optional Persian font support.

---

## 📌 Use Cases
- 🔍 Exploratory Text Analysis (EDA)
- 📊 Visualization of dominant themes in corpora
- 📝 Preprocessing stage for downstream NLP tasks (e.g., classification, sentiment analysis)
- 🌐 Social media data analysis (e.g., Twitter, user reviews, etc.)

---

## 🛠️ Technologies Used
| Purpose           | Library       |
|------------------|---------------|
| Persian NLP       | `hazm`         |
| English NLP       | `nltk`         |
| Visualization     | `matplotlib`, `wordcloud` |
| Text handling     | `re`, `os`, `urllib` |

---

## 📦 Requirements
You can install all required libraries with:

```bash
pip install hazm nltk wordcloud matplotlib
```

And make sure to download required NLTK resources:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

## 📁 Folder Structure

```
.
├── hp_fa.txt                # Raw Persian text
├── hp_en.txt                # Raw English text
├── Processed_hp_fa.txt      # Cleaned Persian text
├── Processed_hp_en.txt      # Cleaned English text
├── Vazir.ttf                # Persian font (for Farsi WordCloud)
└── WordCloud_*.png          # Output WordClouds
```

---

## 🚀 How to Use (In Google Colab or Local)
### 1. Upload raw text files:
- `hp_fa.txt` (Persian)
- `hp_en.txt` (English)
- Optional: `Vazir.ttf` font file

### 2. Run the main script (provided in this repo):
- The script will:
  - preprocess both files separately
  - save the cleaned text
  - generate and display WordClouds

### 3. Output:
- Cleaned `.txt` files
- Two WordClouds (one for Persian, one for English)

---

## 🧾 Persian Preprocessing Steps (using Hazm)
1. Remove extra spaces  
2. Split text into sentences  
3. Normalize text  
4. Tokenize sentences into words  
5. Remove punctuations  
6. Remove stopwords  
7. Remove emojis  
8. Apply **lemmatization**  
9. Generate WordCloud

---

## 🧾 English Preprocessing Steps (using NLTK)
1. Remove extra spaces  
2. Split text into sentences  
3. Convert to lowercase  
4. Tokenize sentences into words  
5. Remove numbers and URLs  
6. Remove punctuation and stopwords  
7. Generate WordCloud

---

## 🌍 Example Output

| Persian WordCloud | English WordCloud |
|------------------|-------------------|
| ![NewFa_WordClouds](https://github.com/user-attachments/assets/64601f8f-f5ea-4637-8d2d-46553b8ff167) | *![NewEn_WordCloud](https://github.com/user-attachments/assets/505694bf-0db5-4ca4-9f7a-8d6877aef5e4)* |
---

## 📄 License
MIT License

---

## 🙌 Acknowledgements
- [Hazm Library](https://github.com/sobhe/hazm)
- [NLTK](https://www.nltk.org/)
- [Vazir Font](https://github.com/rastikerdar/vazir-font)

---

## 📬 Contact
For questions or collaborations, feel free to reach out...
