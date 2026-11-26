import pandas as pd
import re

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load Dataset
df = pd.read_csv(
    "amazon_cells_labelled.txt",
    sep="\t",
    header=None,
    names=["text", "label"]
)

print("Dataset Sample:")
print(df.head())

# Text Preprocessing
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df["clean_text"] = df["text"].apply(clean_text)

print("\nOriginal vs Cleaned:")
print(df[["text", "clean_text"]].head())

# Positive and Negative Examples
print("\nPositive Example:")
print(df[df["label"] == 1]["text"].head())

print("\nNegative Example:")
print(df[df["label"] == 0]["text"].head())

# TF-IDF Feature Extraction
vectorizer = TfidfVectorizer(stop_words="english")

X = vectorizer.fit_transform(df["clean_text"])
y = df["label"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Logistic Regression Model
model = LogisticRegression()

model.fit(X_train, y_train)

# Predictions
