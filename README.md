# Iris Flower Classification using Machine Learning

## Project Overview

This project uses Machine Learning to classify Iris flowers into one of three species:

* Setosa
* Versicolor
* Virginica

The classification is based on four flower measurements:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

The project demonstrates the complete Machine Learning workflow including data loading, visualization, preprocessing, model training, evaluation, and prediction.

---

## Dataset

The project uses the Iris dataset provided by Scikit-Learn.

Dataset Information:

* Total Samples: 150
* Features: 4
* Classes: 3

Target Classes:

| Label | Species    |
| ----- | ---------- |
| 0     | Setosa     |
| 1     | Versicolor |
| 2     | Virginica  |

---

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-Learn

---

## Project Structure

Iris_Flower_Classification/

├── iris_classification.py

├── requirements.txt

└── README.md

---

## Installation

### Clone or Download the Project

```bash
git clone <repository-url>
cd Iris_Flower_Classification
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute the Python file:

```bash
python iris_classification.py
```

---

## Workflow

### 1. Load Dataset

The Iris dataset is loaded using Scikit-Learn.

### 2. Data Exploration

* Display dataset information
* Check missing values
* Generate statistical summaries

### 3. Data Visualization

The following visualizations are created:

* Histograms
* Pair Plots
* Correlation Heatmap

### 4. Train-Test Split

Dataset is divided into:

* Training Data: 80%
* Testing Data: 20%

### 5. Feature Scaling

StandardScaler is used to normalize feature values.

### 6. Model Training

Logistic Regression is used as the classification algorithm.

### 7. Model Evaluation

Performance is measured using:

* Accuracy Score
* Confusion Matrix
* Classification Report

### 8. Prediction

The trained model predicts the species of new flower samples.

---

## Sample Output

```text
Accuracy: 1.0

Confusion Matrix:
[[10 0 0]
 [0 9 0]
 [0 0 11]]

Classification Report:
              precision    recall    f1-score
Setosa          1.00       1.00      1.00
Versicolor      1.00       1.00      1.00
Virginica       1.00       1.00      1.00
```

---

## Skills Learned

* Data Analysis
* Data Visualization
* Feature Scaling
* Classification Algorithms
* Logistic Regression
* Model Evaluation
* Machine Learning Workflow

---

## Future Enhancements

* Compare multiple classification algorithms
* Deploy using Flask or Streamlit
* Create a web interface
* Add real-time user input for predictions

---

## Author

Name: Your Name

Course: MCA

Project: Iris Flower Classification using Machine Learning
