import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

DATA_PATH = "dataset/realestate_vizag.csv"
OUTPUT_DIR = "output"
MODEL_PATH = os.path.join(OUTPUT_DIR, "realestate_model.pkl")

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH).dropna()

X = df[['area', 'bhk', 'bathrooms', 'location']]
y = df['price']

numeric_features = ['area', 'bhk', 'bathrooms']
categorical_features = ['location']

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features),
        ('num', 'passthrough', numeric_features)
    ]
)

pipe = Pipeline(steps=[
    ('prep', preprocessor),
    ('model', LinearRegression())
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipe.fit(X_train, y_train)
score = pipe.score(X_test, y_test)

print(f"Model Accuracy (R2 Score): {score:.4f}")

joblib.dump(pipe, MODEL_PATH)
print(f"Model saved at: {MODEL_PATH}")