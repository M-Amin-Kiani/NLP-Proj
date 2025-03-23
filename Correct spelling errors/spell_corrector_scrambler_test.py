
import re
import requests
from bs4 import BeautifulSoup
from difflib import get_close_matches

# ---------- لود دیکشنری ----------
def load_vocabulary(file_path="Vocabulary.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        return set(line.strip().split()[0].lower() for line in f if line.strip())

# ---------- ارسال جمله به سایت و دریافت جمله خراب‌شده ----------
def get_scrambled_sentence(original_sentence):
    url = "https://www.hakank.org/reading_scrambled_words/g_spell.cgi"
    data = {"input": original_sentence}
    response = requests.post(url, data=data)
    soup = BeautifulSoup(response.text, "html.parser")
    pre_tags = soup.find_all("pre")
    if len(pre_tags) >= 2:
        scrambled = pre_tags[1].text.strip()
        return scrambled
    return None

# ---------- تصحیح کلمات جمله ----------
def correct_word(word, vocab):
    matches = get_close_matches(word, vocab, n=1, cutoff=0.8)
    return matches[0] if matches else word

def correct_sentence(sentence, vocab):
    words = re.findall(r"\b\w+\b", sentence.lower())
    corrected_words = [correct_word(word, vocab) for word in words]
    return " ".join(corrected_words).capitalize() + "."

# ---------- اجرای نهایی ----------
def main():
    vocab = load_vocabulary()
    original = input("Enter a correct English sentence: ").strip()
    scrambled = get_scrambled_sentence(original)

    if scrambled:
        corrected = correct_sentence(scrambled, vocab)
        print("\nOriginal Sentence:")
        print(original)
        print("\nScrambled Sentence (from site):")
        print(scrambled)
        print("\nCorrected Sentence:")
        print(corrected)
    else:
        print("❌ Failed to get scrambled sentence from the site.")

if __name__ == "__main__":
    main()
