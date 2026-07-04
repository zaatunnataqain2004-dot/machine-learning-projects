# Spam Mail Detector using Machine Learning and NLP

## Project Overview

The Spam Mail Detector is a Machine Learning project that classifies messages as either:

* Spam (Unwanted promotional or fraudulent messages)
* Ham (Legitimate messages)

The project uses Natural Language Processing (NLP) techniques to preprocess text data and a Machine Learning model to perform classification.

---

## Objective

To build an intelligent system that can automatically identify spam messages based on their textual content.

---

## Dataset

This project uses the SMS Spam Collection Dataset.

Dataset Features:

* Total Messages: 5,572
* Classes:

  * Ham (Legitimate Messages)
  * Spam (Unwanted Messages)

Example Records:

| Label | Message                              |
| ----- | ------------------------------------ |
| ham   | Hey, are you coming today?           |
| spam  | Congratulations! You have won $1000. |

---

## Technologies Used

* Python
* NumPy
* Pandas
* NLTK
* Scikit-Learn
* Matplotlib
* Seaborn

---

## Machine Learning Concepts Used

### Natural Language Processing (NLP)

* Lowercasing
* Punctuation Removal
* Stopword Removal
* Tokenization

### Feature Extraction

* TF-IDF Vectorization

### Classification Algorithm

* Multinomial Naive Bayes

### Evaluation Metrics

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## Project Structure

Spam_Mail_Detector/

├── spam_detector.py

├── spam.csv

├── requirements.txt

└── README.md

---

## Installation

### Step 1: Clone or Download the Project

```bash id="6d9b0k"
git clone <repository-url>
cd Spam_Mail_Detector
```

### Step 2: Install Required Libraries

```bash id="fpkcyk"
pip install -r requirements.txt
```

---

## Running the Project

Execute the Python file:

```bash id="n5lsw2"
python spam_detector.py
```

---

## Project Workflow

### 1. Load Dataset

The SMS dataset is loaded using Pandas.

### 2. Data Cleaning

Text preprocessing includes:

* Convert text to lowercase
* Remove punctuation
* Remove stopwords

Example:

Before:

```text id="9p2w8m"
Congratulations! You have won $1000.
```

After:

```text id="e75yur"
congratulations won 1000
```

### 3. Feature Extraction

TF-IDF converts text into numerical vectors suitable for Machine Learning algorithms.

### 4. Train-Test Split

Dataset is divided into:

* Training Data: 80%
* Testing Data: 20%

### 5. Model Training

Multinomial Naive Bayes is trained using the processed message vectors.

### 6. Prediction

The model predicts whether a message is spam or ham.

### 7. Evaluation

Performance is evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## Sample Output

```text id="2y9vl8"
Accuracy: 0.98

Classification Report:

              precision    recall  f1-score

Ham             0.99       0.99      0.99
Spam            0.96       0.95      0.95

Overall Accuracy: 98%
```

---

## Example Prediction

Input:

```text id="v4jvz4"
Congratulations! You won a free iPhone.
```

Output:

```text id="mvnbgb"
Spam
```

Input:

```text id="jlwm2t"
Can we meet at 5 PM today?
```

Output:

```text id="jjukj0"
Ham
```

---

## Skills Learned

* Natural Language Processing (NLP)
* Text Preprocessing
* Stopword Removal
* Feature Engineering
* TF-IDF Vectorization
* Naive Bayes Classification
* Model Evaluation
* Spam Detection Systems

---

## Future Enhancements

* Build a Web Application using Flask
* Create a Streamlit Dashboard
* Use Advanced NLP Techniques
* Train with Larger Email Datasets
* Compare Multiple Models:

  * Logistic Regression
  * Support Vector Machine (SVM)
  * Random Forest
  * XGBoost

---

## Expected Accuracy

The model typically achieves:

* 95% to 99% Accuracy

depending on preprocessing and dataset quality.

---

## Author

Name: Your Name

Course: MCA

Project Title: Spam Mail Detector using Machine Learning and NLP

Academic Year: 2026
