import pandas as pd
import nltk
import string

from nltk.corpus import stopwords

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

import seaborn as sns
import matplotlib.pyplot as plt

nltk.download('stopwords')

df = pd.read_csv(
    "spam.csv",
    encoding="latin-1"
)

df = df[['v1','v2']]
df.columns = ['label','message']

df['label'] = df['label'].map({
    'ham':0,
    'spam':1
})

def clean_text(text):

    text = text.lower()

    text = ''.join(
        char for char in text
        if char not in string.punctuation
    )

    words = text.split()

    words = [
        word for word in words
        if word not in stopwords.words('english')
    ]

    return " ".join(words)

df['clean_message'] = df['message'].apply(clean_text)

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(
    df['clean_message']
)

y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = MultinomialNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:",
      accuracy_score(y_test, y_pred))

print(classification_report(
    y_test,
    y_pred
))

cm = confusion_matrix(
    y_test,
    y_pred
)

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues'
)

plt.show()

sample = [
    "Congratulations! You won a free iPhone"
]

sample = [clean_text(msg)
          for msg in sample]

sample_vector = vectorizer.transform(
    sample
)

prediction = model.predict(
    sample_vector
)

if prediction[0] == 1:
    print("Spam")
else:
    print("Ham")