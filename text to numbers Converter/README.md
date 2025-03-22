
# 🔁 Universal Number ↔ Text Converter (English + Persian)

This is a smart, dual-language CLI tool that **automatically detects and converts** between numeric digits and written numbers in **Persian (فارسی)** and **English**, with support for:
- ✅ Integer numbers (صحیح)
- ✅ Decimal numbers (اعشاری)
- ✅ Negative numbers (منفی / negative)
- 🔤 Bidirectional conversion (Text → Number & Number → Text)

---

## 📦 Installation

Before using, install required libraries:

```bash
pip install hazm
pip install num2fawords
pip install word2number
pip install num2words
```

---

## 🚀 How to Use

Simply run the Python script and enter your input. It will detect the language and input type automatically.

### ▶️ Example Inputs:

#### 🔹 Persian:
| Input | Output |
|-------|--------|
| سه میلیون و پانصد | 3,000,500 |
| منفی چهار هزار و بیست و یک | -4,021 |
| دوازده ممیز پنجاه و سه | 12.53 |

#### 🔸 English:
| Input | Output |
|-------|--------|
| one hundred twenty-five thousand | 125,000 |
| negative five point seventy-five | -5.75 |
| 123456 | one hundred twenty-three thousand four hundred fifty-six |

---

## 📜 Features

- 🧠 **Language Auto Detection** (based on script)
- 🔄 **Two-Way Conversion** (text ↔ number)
- 🌐 **Supports English and Persian**
- 🔣 Handles **decimals and negative numbers**
- 🧪 Pure Python & CLI-based (no voice/sound dependencies)

---

## 🧩 Example Usage

```bash
$ python converter.py
🔸 عدد یا متن عددی وارد کنید (فارسی یا انگلیسی):
> پنج هزار و سیصد و شصت و هفت
🔹 خروجی: 5,367
```

---

## 📁 Files

- `converter.py` → Main script for bidirectional conversion.
- `README.md` → You are here!

---

## 🛠 Future Ideas

- GUI with Tkinter or Web UI with Streamlit
- Batch conversion via file
- Telegram or WhatsApp Bot integration

---

## 👤 Author

Created with ❤️ by an awesome developer and ChatGPT.
