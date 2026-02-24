# 🏠 AI System for Real Estate Price Prediction

This project predicts house prices based on **area (sqft), BHK,
bathrooms, and location** using Machine Learning.\
It includes: - ✅ Model training pipeline (Scikit-learn) - ✅ REST API
using Flask - ✅ Interactive UI using Streamlit - ✅ Ready-to-deploy
project structure

------------------------------------------------------------------------

## 📁 Project Structure

    AI_System_for_Realestate_Price_Prediction/
    │
    ├── .venv/
    ├── dataset/
    │   └── realestate.csv
    ├── output/
    │   └── realestate_model.pkl
    ├── scripts/
    │   ├── main.py     # Train ML model
    │   ├── app.py      # Flask API
    │   └── ui.py       # Streamlit UI
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## ⚙️ Setup (One-Time)

### 1️⃣ Install Python 3.11+

Download: https://www.python.org/downloads/

### 2️⃣ Create Virtual Environment

``` bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🚀 How to Run

### 🔹 Train the Model

``` bash
python scripts/main.py
```

This will create:

    output/realestate_model.pkl

------------------------------------------------------------------------

### 🔹 Run Flask API

``` bash
python scripts/app.py
```

API will start at:

    http://127.0.0.1:5000

------------------------------------------------------------------------

### 🔹 Run Streamlit UI

``` bash
streamlit run scripts/ui.py
```

Open in browser:

    http://localhost:8501

------------------------------------------------------------------------

## 🔌 API Usage (Flask)

### Endpoint

    POST /predict

### Sample Request (JSON)

``` json
{
  "area": 1200,
  "bhk": 2,
  "bathrooms": 2,
  "location": "Adyar"
}
```

### Sample Response

``` json
{
  "predicted_price": 12500000
}
```

------------------------------------------------------------------------

## 🖥️ UI Usage (Streamlit)

1.  Enter:
    -   Area (sqft)
    -   BHK
    -   Bathrooms
    -   Location
2.  Click **Predict Price**
3.  View predicted house price

------------------------------------------------------------------------

## 📸 Screenshots

> Add screenshots of: - Model training output - Flask API response
> (Postman) - Streamlit UI page

Example:

    /screenshots/ui.png
    /screenshots/api.png

------------------------------------------------------------------------

## 🧠 Tech Stack

-   Python 3.11\
-   Pandas\
-   Scikit-learn\
-   Flask\
-   Streamlit\
-   Joblib

------------------------------------------------------------------------

## 📌 Features

-   End-to-end ML pipeline\
-   OneHotEncoding for locations\
-   REST API deployment\
-   User-friendly web UI\
-   GitHub-ready project

------------------------------------------------------------------------

## 🧪 Model Details

-   Algorithm: Linear Regression\
-   Categorical Encoding: OneHotEncoder\
-   Evaluation Metric: R² Score

------------------------------------------------------------------------

## 📤 Upload to GitHub

``` bash
git init
git add .
git commit -m "AI Real Estate Price Prediction"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/AI-Realestate-Price-Prediction.git
git push -u origin main
```

------------------------------------------------------------------------

## 👤 Author

Your Name\
GitHub: https://github.com/YOUR_USERNAME\
LinkedIn: https://linkedin.com/in/YOUR_PROFILE

------------------------------------------------------------------------

⭐ If you like this project, give it a star on GitHub!
