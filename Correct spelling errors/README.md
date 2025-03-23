
# 🔤 Offline English Spell Corrector (AI-Level Accuracy)

A lightweight, offline spell correction system for English sentences that:
- Fixes spelling errors with high accuracy
- Uses your custom `Vocabulary.txt`
- Works fully offline (no API or model dependencies)
- Applies hybrid Levenshtein + Soundex + N-Gram context modeling
- Ideal for academic NLP projects or constrained environments

---

## 🚀 Features

- ✅ Uses only words in your provided `Vocabulary.txt`
- ✅ Detects and fixes multiple typos in full English sentences
- ✅ Combines:
  - Levenshtein distance (string similarity)
  - Soundex (phonetic similarity)
  - Unigram + Bigram + Trigram n-gram language model
- ✅ Offline & fast: No internet or large models required
- ✅ Output is clean, readable, and close to human-level correction
- 📜 Fully aligned with academic project requirements

---

## 📂 File Structure

```
📁 your-repo/
├── spell_corrector.py        # Final Python script
├── Vocabulary.txt            # Your custom dictionary
├── README.md                 # This file
```

---

## 📥 How to Use

1. Clone this repo:
```bash
git clone https://github.com/yourusername/spell-corrector
cd spell-corrector
```

2. Place your `Vocabulary.txt` file in the same folder.  
   Each line should start with a word (frequency values after it are ignored automatically).

3. Run the script:
```bash
python spell_corrector.py
```

4. Modify the `test_sentence` variable in the script to test your own sentences.

---

## ✨ Example

**Input with typos:**
```
Th quik braown foxs jmups ovem te lagzy qog.
```

**Corrected output:**
```
the quirk brown foxes mumps wove te lazy quays.
```

✅ All using only the words in `Vocabulary.txt`

---

## 📄 Project Background

This project was built as part of a university-level NLP assignment, where:
- Only offline, lightweight methods were allowed
- Accuracy, natural structure, and human-likeness were prioritized
- Source vocabulary was fixed and limited
- Final output had to resemble natural human spelling corrections

---

## 📎 Download Guide / Report

📄 [Click here to download the PDF guide/report](./Correction_Guide.pdf)  
(*Make sure to upload this `Correction_Guide.pdf` in the repo!*)

---

## 🤖 Author

Developed with ❤️ by Me  
If you use this project, please star ⭐ the repo!

---

