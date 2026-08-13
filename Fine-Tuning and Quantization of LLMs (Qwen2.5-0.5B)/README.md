# 🚀 Fine-Tuning and Quantization of LLMs (Qwen2.5-0.5B)

This project provides a comprehensive exploration, implementation, and comparison of **Quantization** and **Parameter-Efficient Fine-Tuning (PEFT)** methods on the **Qwen2.5-0.5B-Instruct** large language model. The primary objective is to optimize the model for **Sentiment Analysis** using the Persian dataset `hezarai/sentiment-dksf`.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Key Concepts & Theory](#-key-concepts--theory)
- [Part 1: Model Quantization](#part-1-model-quantization)
- [Part 2: Fine-Tuning with QLoRA](#part-2-fine-tuning-with-qlora)
- [Part 3: Fine-Tuning with Prefix Tuning](#part-3-fine-tuning-with-prefix-tuning)
- [Final PEFT Comparison](#-final-peft-comparison)
- [Error Analysis](#-error-analysis)
- [Repository Structure & Adapters](#-repository-structure--adapters)

---

## 📖 Project Overview

Large Language Models (LLMs) demand massive hardware resources (VRAM) despite their high intelligence. This project addresses two major challenges:

1. **How can we make the model smaller?** Evaluating quantization across 4 precision levels (`FP16`, `INT8`, `NF4`, `INT4`).
2. **How can we train the model with minimal hardware costs?** Comparing two prominent PEFT techniques: **QLoRA** and **Prefix Tuning**.

- **Base Model:** `Qwen/Qwen2.5-0.5B-Instruct`
- **Dataset:** `hezarai/sentiment-dksf` (Train: 28,602 | Test: 2,315)
- **Main Task:** Sentiment classification of user reviews (Positive, Negative, Neutral)

---

## 📚 Key Concepts & Theory

- **Inductive Bias:** The set of assumptions a learning algorithm uses to predict outputs of given inputs that it has not encountered.
- **Quantization:** Compressing the model by reducing the precision of its weights (e.g., converting 32-bit or 16-bit floats to 4-bit integers) to heavily reduce VRAM usage.
- **NF4 (Normal Float 4):** A specialized 4-bit quantization data type for neural networks that reduces model size by up to 75% without significant accuracy degradation.
- **LoRA / QLoRA:** Low-Rank Adaptation involves training two small matrices ($r$) instead of updating all parameters of the base model.
- **Prefix Tuning:** Injecting virtual tokens into the model's layers without altering the internal weights.
- **VRAM:** Video RAM; the dedicated memory on a GPU where the model is loaded for execution and training.

---

## Part 1: Model Quantization

In this section, the base model's performance was evaluated across 4 precision levels on 3 distinct tasks (Translation, Summarization, and Sentiment Analysis).

### 📊 Precision Comparison Table

| Precision | Peak VRAM (GB) | Latency (sec) [Trans / Sum / Sent] | Tokens/sec [Trans / Sum / Sent] | Sentiment Output |
| :-------: | :------------: | :--------------------------------: | :-----------------------------: | :--------------: |
| **FP16**  |    3.30 GB     |         0.68 / 5.70 / 0.17         |      22.16 / 22.46 / 23.84      | منفی (Negative)  |
| **INT8**  |    2.98 GB     |        5.00 / 44.29 / 1.89         |       2.00 / 2.12 / 2.12        | منفی (Negative)  |
|  **NF4**  |  **2.83 GB**   |        2.41 / 11.89 / 0.40         |      10.35 / 10.76 / 10.00      | منفی (Negative)  |
| **INT4**  |    3.02 GB     |        6.38 / 11.43 / 0.37         |      10.50 / 11.20 / 10.68      | منفی (Negative)  |

### 💡 Quantization Analysis

- **Most Resilient Task:** `Sentiment Analysis`; the model successfully generated the correct output across all quantization levels with high speed.
- **Most Vulnerable Task:** `Summarization`; at lower precisions (like NF4/INT4), the model suffered from text coherence degradation and word repetition.
- **Conclusion:** The **NF4** format offers the best balance, successfully reducing VRAM consumption to 2.83 GB while maintaining an acceptable generation speed.

---

## Part 2: Fine-Tuning with QLoRA

To specialize the model in Persian sentiment classification, the base model was fine-tuned using the QLoRA technique.

### ⚙️ Training Configuration

- **Trainable Parameters:** `8,798,208` (**1.75%** of total model parameters)
- **Epochs:** `1`
- **Batch Size / Accumulation:** `4 / 2`
- **Learning Rate:** `2e-4`

### 🎯 QLoRA Evaluation Results

| Metric       |   Score    |
| :----------- | :--------: |
| **Accuracy** | **83.40%** |
| **F1-Macro** | **0.7044** |

> **Before Fine-Tuning:** The model generated unstructured outputs and struggled with domain-specific vocabulary.  
> **After Fine-Tuning:** The model achieved an impressive **83.40%** accuracy, producing highly standardized and exact labels.

---

## Part 3: Fine-Tuning with Prefix Tuning

Instead of updating internal weights, this method injects 30 continuous virtual tokens into the prompts.

### ⚙️ Training Configuration

- **Trainable Parameters:** `184,320` (Only **0.037%** of total model parameters)
- **Learning Rate:** `2e-3`
- **Loss Masking:** Applied `-100` labels to the prompt tokens so the loss is calculated _only_ on the final generated label.

### 🎯 Prefix Tuning Evaluation Results

| Metric       |   Score    |
| :----------- | :--------: |
| **Accuracy** | **67.20%** |
| **F1-Macro** | **0.4820** |

---

## ⚖️ Final PEFT Comparison

| PEFT Method       |  Accuracy  |  F1-Macro  | Training Time |  Peak VRAM  | Trainable Parameters |
| :---------------- | :--------: | :--------: | :-----------: | :---------: | :------------------: |
| **QLoRA**         | **83.40%** | **0.7044** |  108.7 mins   |   ~4.0 GB   |  8,798,208 (1.75%)   |
| **Prefix Tuning** | **67.20%** | **0.4820** | **28.9 mins** | **~3.1 GB** | **184,320 (0.037%)** |

### 🔍 Conclusion & Final Recommendation:

1. **Performance & Accuracy:** **QLoRA** significantly outperforms Prefix Tuning (by ~16% in accuracy) because updating the attention weights enables deeper linguistic understanding, especially for small models (0.5B).
2. **Resource Consumption:** **Prefix Tuning** requires less memory and is almost 4 times faster to train, but limits the reasoning capacity of smaller models.
3. **Final Recommendation:** **QLoRA** is the superior choice for practical deployments. Combined with 4-bit quantization (NF4), it allows training highly accurate models on budget-friendly or free GPUs (like Colab T4).

---

## 🔍 Error Analysis

An in-depth review of the misclassified samples by the QLoRA model revealed the following primary causes:

1. **Implicit Sentiment & Sarcasm:** Sentences with advising tones (e.g., "Raise the price but don't lower the quality") were sometimes misinterpreted as negative.
2. **Label Noise in Dataset:** Some test samples were clearly negative reviews (e.g., complaining about stale bread) but were incorrectly tagged as `neutral` in the original dataset. The model's prediction (`negative`) was actually more accurate than the ground truth.
3. **Domain-Specific Vocabulary:** Technical terms or specific market jargon occasionally misled the model's sentiment weighting.

---

## 🛡️ Scientific Principles & Data Integrity

- **Data Isolation:** The Train/Test split was strictly isolated before any tokenization or preprocessing, completely avoiding **Data Leakage**.
- **Deterministic Evaluation:** To ensure full reproducibility without arbitrary seeds, the evaluation was performed on a fixed sequential subset (first 500 records) of the shuffled test set.

---

## 📂 Repository Structure & Adapters

Following the fine-tuning process, only the lightweight adapter weights were saved, eliminating the need to duplicate the massive base model:

- `adapter_qlora/adapter_model.safetensors` (~35 MB)
- `adapter_prefix_optimized/adapter_model.safetensors` (~0.7 MB)
