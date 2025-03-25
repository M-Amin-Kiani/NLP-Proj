
# Fake News Detection with Text Classification

This repository contains code for detecting fake news using text classification techniques. The project uses two main models: **KNN** (K-Nearest Neighbors) and **SVM** (Support Vector Machines), along with two different text preprocessing and vectorization methods: **TF-IDF** and **Text-to-Sequence**. The project is implemented using Python and popular libraries such as TensorFlow, scikit-learn, and NLTK.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Data](#data)
- [Usage](#usage)
  - [Preprocessing](#preprocessing)
  - [Model Training and Evaluation](#model-training-and-evaluation)
- [Models](#models)
  - [KNN Model](#knn-model)
  - [SVM Model](#svm-model)
- [Results](#results)
- [License](#license)

## Overview
The goal of this project is to classify news articles as **real** or **fake** based on their content. The main focus of the project is on feature extraction and applying machine learning algorithms to classify the news articles.

This repository includes:
- Data loading, preprocessing, and vectorization using **TF-IDF** and **Text-to-Sequence**.
- Model training using **KNN** and **SVM** algorithms.
- Evaluation of the models using common classification metrics such as **Accuracy**, **Precision**, **Recall**, and **F1 Score**.

## Requirements
The following libraries are required to run the code:
- Python 3.6+
- **TensorFlow** (for neural networks and deep learning models)
- **scikit-learn** (for machine learning models and metrics)
- **NLTK** (for text preprocessing)
- **pandas** (for data manipulation)
- **NumPy** (for numerical operations)

You can install the necessary libraries using `pip`:

```bash
pip install tensorflow scikit-learn nltk pandas numpy
```

## Installation
Clone this repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/fake-news-detection.git
cd fake-news-detection
```

## Data
The dataset used in this project consists of two files:
1. `true.csv` - Contains real news articles.
2. `fake.csv` - Contains fake news articles.

These CSV files must include the following columns:
- **title**: Title of the news article.
- **text**: Content of the news article.
- **subject**: Subject category of the news article.
- **date**: Date of publication.
- **label**: Target label (1 for real, 0 for fake).

## Usage

### Preprocessing
The code preprocesses the text data by performing the following steps:
1. **Lowercasing**: Converts all text to lowercase.
2. **Removing extra spaces**: Removes any extra spaces from the text.
3. **Tokenization**: Splits the text into sentences and words.
4. **Removing numbers and URLs**: Removes any numbers and URLs from the text.
5. **Removing stopwords and punctuation**: Eliminates common stopwords and punctuation marks.

After preprocessing, the text data is transformed into numerical representations.

### Model Training and Evaluation

The main steps in the code are:
1. **Vectorization**: 
   - The text data is converted into a numerical format using either **TF-IDF** or **Text-to-Sequence** methods.
   - TF-IDF is used for **feature extraction**, and **Text-to-Sequence** is used when working with sequential models.
2. **Model Training**:
   - The **KNN** and **SVM** models are trained on the vectorized data.
3. **Model Evaluation**:
   - The models are evaluated on the validation and test sets, and classification metrics such as **Accuracy**, **Precision**, **Recall**, and **F1 Score** are calculated.

### KNN Model
The **KNN** (K-Nearest Neighbors) model is a simple and effective algorithm for classification. It works by finding the most similar points in the feature space and predicting the class based on the majority of the nearest neighbors.

### SVM Model
The **SVM** (Support Vector Machines) is a powerful algorithm for classification tasks. It tries to find the best hyperplane that separates the classes with the maximum margin. In this project, we use a linear SVM and an RBF (Radial Basis Function) kernel.

## Results

### KNN Model Results on Validation:
- **Accuracy**: 52.55%
- **Precision**: 0.0 (may indicate poor model performance, revisit preprocessing or hyperparameters)
- **Recall**: 0.0 (may indicate poor model performance, revisit preprocessing or hyperparameters)
- **F1 Score**: 0.0

### SVM Model Results on Validation:
- **Accuracy**: Higher than KNN (depending on kernel)
- **Precision, Recall, and F1**: Metrics calculated similarly.

### Final Comparison on Test Data:
```plaintext
Model    Accuracy    Precision    Recall    F1 Score
----------------------------------------------------
KNN      0.5255      0.0          0.0       0.0
SVM      X.XXXX      X.XXXX       X.XXXX    X.XXXX
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute or open issues if you have any questions or suggestions!

---

### Important Notes:
- If your model’s **precision** and **recall** are 0, it might be due to improper data preprocessing, incorrect model configuration, or issues in hyperparameter tuning.
- You can experiment with different **vectorizer settings** (like `min_df`, `max_df`) or **model hyperparameters** (like `n_neighbors` for KNN or kernel types for SVM) to improve performance.
