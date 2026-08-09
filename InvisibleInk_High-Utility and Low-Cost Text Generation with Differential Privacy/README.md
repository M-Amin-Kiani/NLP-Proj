# InvisibleInk: High-Utility & Low-Cost Differentially Private Text Generation

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.1%2B-ee4c2c.svg)](https://pytorch.org/)
[![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg)](https://huggingface.co/docs/transformers/index)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Domain](https://img.shields.io/badge/NLP-Differential%20Privacy-purple.svg)]()

> **Master's Research Project in Natural Language Processing (NLP)**  
> **University of Isfahan — Department of Artificial Intelligence**

An in-depth study, experimental evaluation, and architectural enhancement suite for **InvisibleInk** (*High-Utility and Low-Cost Text Generation with Differential Privacy*). This repository contains detailed theoretical analysis, local experimental execution logs using `TinyLlama-1.1B`, and three novel proposed research extensions aiming to further accelerate DP decoding and optimize dynamic privacy budgeting.

---

## 📌 Table of Contents
- [1. Executive Summary](#1-executive-summary)
- [2. Problem Statement](#2-problem-statement)
- [3. Core Architecture & Innovations of InvisibleInk](#3-core-architecture--innovations-of-invisibleink)
  - [3.1 Targeted Clipping (DClip)](#31-targeted-clipping-dclip)
  - [3.2 Truncated Top-$k^+$ Sampling](#32-truncated-top-k-sampling)
- [4. Experimental Results & Local Reproduction](#4-experimental-results--local-reproduction)
- [5. Critical Analysis & Model Limitations](#5-critical-analysis--model-limitations)
- [6. Proposed Research Innovations (Our Enhancements)](#6-proposed-research-innovations-our-enhancements)
  - [Idea 1: Speculative Decoding for DP-LLMs](#idea-1-speculative-decoding-for-dp-llms)
  - [Idea 2: Reference Condensation Attention Module](#idea-2-reference-condensation-attention-module)
  - [Idea 3: Entropy-Aware Dynamic Clipping Norm ($C_t$)](#idea-3-entropy-aware-dynamic-clipping-norm-c_t)
- [7. Project Setup & Quickstart](#7-project-setup--quickstart)
- [8. Repository Structure](#8-repository-structure)
- [9. Citation & References](#9-citation--references)

---

## 1. Executive Summary

Retrieval-Augmented Generation (RAG) and private text synthesis allow Large Language Models (LLMs) to generate contextualized responses using sensitive databases (e.g., medical records, legal proceedings, financial contracts). However, traditional Differential Privacy (DP) mechanisms suffer from two major bottlenecks:
1. **Enormous Computational Overhead:** Requiring up to 100× forward passes per generated token compared to standard non-private decoding.
2. **Severe Utility Loss:** Standard DP sampling from the entire vocabulary introduces massive noise, yielding ungrammatical or nonsensical output.

**InvisibleInk** addresses these challenges by shifting DP mechanism design from training-time modifications to **inference-time logit processing**, delivering a **8× to 16× reduction in computational cost** while maintaining state-of-the-art text quality (utility).

---

## 2. Problem Statement

Given a set of $B$ private reference texts $R = \{r_1, r_2, \dots, r_B\}$ and a public prompt/context, an autoregressive language model $M$ generates logits $\phi_i$ for each reference $i \in \{1, \dots, B\}$ alongside public baseline logits $\phi_{	ext{pub}}$.

$$ \phi_i = M(r_i, x_{<t}), \quad \phi_{	ext{pub}} = M(\emptyset, x_{<t}) $$

Existing DP sampling techniques apply noise across all $|V|$ vocabulary tokens across all references, leading to:
- High sensitivity bounded by $B$.
- Extremely slow inference due to independent forward passes.
- Low-utility text resulting from uniform high-temperature sampling across noisy long-tail logits.

---

## 3. Core Architecture & Innovations of InvisibleInk

```
                       ┌──────────────────────────────┐
                       │   Private References (R)     │
                       └──────────────┬───────────────┘
                                      │
                                      ▼
┌─────────────────┐            ┌──────────────┐            ┌───────────────────────┐
│ Public Context  ├───────────►│ Logit Engine ├───────────►│ DClip & Noise (DP)    │
└─────────────────┘            └──────────────┘            └──────────┬────────────┘
                                                                      │
                                                                      ▼
┌─────────────────┐            ┌──────────────┐            ┌───────────────────────┐
│ Generated Text  │◄───────────┤ Next Token   │◄───────────┤ Truncated Top-k+      │
└─────────────────┘            └──────────────┘            └───────────────────────┘
```

InvisibleInk introduces two core algorithmic mechanisms during autoregressive decoding:

### 3.1 Targeted Clipping (DClip)
Instead of clipping raw private logits $\phi_i$ directly, DClip isolates the incremental private knowledge by subtracting the public logit vector $\phi_{	ext{pub}}$. Clipping is applied solely to the private-public difference:

$$	ext{DClip}_C(\phi_i, \phi_{	ext{pub}}) := \phi_{	ext{pub}} + 	ext{clip}_C(\phi_i - \phi_{	ext{pub}})$$

Where $	ext{clip}_C(v) = v \cdot \min\left(1, rac{C}{\|v\|_2}
ight)$.  
* **Why it works:** Public logits already capture natural language grammar, syntax, and general world knowledge. By clipping only the delta $(\phi_i - \phi_{	ext{pub}})$, sensitivity is drastically bounded without destroying linguistic coherence.

### 3.2 Truncated Top-$k^+$ Sampling
Standard Top-$k$ filtering breaks DP guarantees if the candidate set depends on private logits. InvisibleInk constructs a deterministic public candidate superset $V_k^+$ derived from $\phi_{	ext{pub}}$ using a logit threshold:

$$l_{	ext{thresh}} = l_{(k)} - rac{2C}{B}$$

Any token with a public logit exceeding $l_{	ext{thresh}}$ is included in $V_k^+$. This guarantees that top private tokens are retained in $V_k^+$ without leaking additional private budget.

---

## 4. Experimental Results & Local Reproduction

### Paper Benchmarks
- **Hardware:** 4× NVIDIA RTX L40S (48GB) / NVIDIA H100 (80GB).
- **Models Evaluated:** `TinyLlama-1.1B-Chat` and `LLaMA-3-8B`.
- **Metrics:** MAUVE (distributional text quality) and MedNER (entity extraction utility).
- **Key Finding:** Achieved high-utility long-form private text synthesis with an 8×–16× reduction in batch execution budget $B$.

### Local Empirical Verification
We executed a local test run utilizing PyTorch 2.11 with CUDA acceleration on the Text Anonymization Benchmark (TAB) legal corpus.

```text
Dataset: ECHR Court Cases (TAB)
Model: TinyLlama/TinyLlama-1.1B-Chat-v1.0
Hardware Acceleration: CUDA (PyTorch 2.11.0+cu128)
Epsilon Spent: [8.1159, 10.0]
Average Candidate Superset Size (Top-k+): 114.73 tokens
Throughput / Execution Speed: ~11.53 sec/iteration (2 complete sequences generated in 23s)
```

**Local Generation Sample:**
> *"The text sample could belong to the dataset 'European Court of Human Rights (ECHR)' as it describes English-language court cases from this court, making it suitable for the given task..."*

---

## 5. Critical Analysis & Model Limitations

1. **White-Box Access Prerequisite:** Requires direct access to internal output logit vectors $\phi_i$. Consequently, it cannot be deployed over closed-source API-only models (e.g., GPT-4, Claude 3.5).
2. **Model Alignment & Safety Conflicts:** Testing on instruction-tuned models like `LLaMA-3-8B-Instruct` revealed safety-triggering artifacts. When generating private sensitive text, RLHF alignment mechanisms occasionally intervened, generating disclaimers or defensive outputs.
3. **Linear Forward Overhead ($B+1$):** Despite optimizations, each output token still requires $B$ private passes plus $1$ public pass per step, posing latency challenges for edge devices.

---

## 6. Proposed Research Innovations (Our Enhancements)

To mitigate the limitations identified above, we propose three theoretical and architectural extensions:

```
                          ┌──────────────────────────────────────────────┐
                          │     PROPOSED RESEARCH EXTENSIONS             │
                          └──────────────────────┬───────────────────────┘
                                                 │
          ┌──────────────────────────────────────┼──────────────────────────────────────┐
          │                                      │                                      │
          ▼                                      ▼                                      ▼
┌───────────────────┐                  ┌───────────────────┐                  ┌───────────────────┐
│ Proposal 1        │                  │ Proposal 2        │                  │ Proposal 3        │
│ Speculative       │                  │ Reference         │                  │ Entropy-Aware     │
│ Decoding          │                  │ Condensation Attn │                  │ Dynamic Ct        │
└───────────────────┘                  └───────────────────┘                  └───────────────────┘
```

### Idea 1: Speculative Decoding for DP-LLMs
* **Concept:** Deploy a lightweight Draft Model $M_{	ext{draft}}$ to predict candidate tokens based on public logits $\phi_{	ext{pub}}$.
* **Mechanism:** Calculate the entropy $\mathcal{H}(\phi_{	ext{pub}})$. For low-entropy steps (standard syntax/grammar), accept draft tokens directly without triggering the full $B+1$ private LLM pass.
* **Impact:** Drastically reduces total forward passes, breaking the linear dependence on $B$ for predictable tokens.

### Idea 2: Reference Condensation Attention Module
* **Concept:** Insert a cross-attention condensation module before entering the main LLM layers.
* **Mechanism:** Instead of running $B$ individual sequences through the model, $B$ private reference embeddings are compressed into $B' \ll B$ dense latent representations using a trainable private cross-attention block.
* **Impact:** Shifts private aggregation from logit space to latent space, reducing memory footprint and forward pass complexity.

### Idea 3: Entropy-Aware Dynamic Clipping Norm ($C_t$)
* **Concept:** Replace the static clipping parameter $C$ with a dynamic, token-level clipping norm $C_t$.
* **Formula:**
  $$C_t = lpha \cdot \mathcal{H}(\phi_{	ext{pub}}) = lpha \cdot \left( - \sum_{w \in V} P_{	ext{pub}}(w) \log P_{	ext{pub}}(w) 
ight)$$
* **Impact:** Automatically allocates more privacy budget (larger $C_t$) when public confidence is low (domain-specific entity tokens), and tightens clipping (smaller $C_t$) when public model confidence is high.

---

## 7. Project Setup & Quickstart

### Environment Setup
```bash
# Clone the repository
git clone https://github.com/your-username/invisibleink-nlp-project.git
cd invisibleink-nlp-project

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scriptsctivate

# Install dependencies
pip install torch transformers datasets invink tqdm pandas
```

### Execution Script
```python
import torch
import invink
from datasets import load_dataset

def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Executing InvisibleInk on device: {device}")
    
    # Load sample reference dataset
    dataset = load_dataset("mattmdjaga/text-anonymization-benchmark-train")
    references = dataset["train"]["text"][:8]
    
    # Generate DP private text
    output = invink.generate(
        references=references,
        model_name_or_path="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        num=2,
        epsilon=10.0,
        batch_size=8,
        max_toks=150,
        dataset_desc="ECHR Court Cases Anonymization"
    )
    
    for idx, text in enumerate(output.texts):
        print(f"\n--- Sample {idx+1} ---")
        print(text)

if __name__ == "__main__":
    main()
```

---

## 8. Repository Structure

```text
.
├── README.md               # Comprehensive project documentation
├── requirements.txt        # Python package dependencies
├── src/
│   ├── main.py             # Inference pipeline script
│   ├── dclip.py            # Custom DClip & Top-k+ logit processor implementation
│   └── dynamic_norm.py     # Proposal 3: Entropy-aware dynamic clipping
├── docs/
│   ├── presentation.pdf    # Slide deck for project defense
│   └── research_paper.pdf  # InvisibleInk reference paper
└── logs/
    └── execution_log.txt   # PyTorch execution benchmark logs
```

---

## 9. Citation & References

```bibtex
@inproceedings{invisibleink2024,
  title={InvisibleInk: High-Utility and Low-Cost Text Generation with Differential Privacy},
  author={Amin, Saad and et al.},
  booktitle={Proceedings of the Association for Computational Linguistics (ACL)},
  year={2024}
}
```

---
*Developed as part of the Graduate Natural Language Processing Course — University of Isfahan.*
