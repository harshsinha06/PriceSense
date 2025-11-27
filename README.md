# 🏠 PriceSense — Real Estate Price Prediction Tool

**PriceSense** is a web-based application that predicts **property prices in Bengaluru** based on features like **BHK, location, and amenities**.  
It combines a **Flask backend** powered by **machine learning** with an **interactive frontend** built using **HTML, CSS, and JavaScript**.

---

## 🚀 Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python (Flask)  
- **Machine Learning:** scikit-learn  
- **Model:** Multiple Linear Regression  

---

## 📊 Project Overview

- 🏗 **Purpose:** To provide accurate, data-driven predictions for Bengaluru real estate prices.  
- 🤖 **Model Performance:** Achieved an **R² score of 0.85** on the test dataset — indicating strong predictive capability.  
- 💡 **Features:**
  - Real-time price prediction through a simple and clean web interface.  
  - Trained ML model using Bengaluru housing dataset.  
  - Interactive UI for inputting location, BHK, and amenities.  
  - Dynamic response displaying predicted prices instantly.

---

## ⚙️ How It Works

1. User inputs **location**, **number of BHKs**, and **amenities** via the web form.  
2. The data is sent to the **Flask backend**.  
3. The **trained regression model** processes the input and returns a price prediction.  
4. The **frontend** displays the predicted property price dynamically.

---

## 🧩 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/PriceSense.git
cd PriceSense
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask app
```bash
python app.py
```

### 5. Open in browser  
Visit 👉 **http://127.0.0.1:5000**

---

## 📈 Example Prediction

| Location      | BHK | Amenities | Predicted Price (₹) |
|----------------|-----|------------|---------------------|
| Whitefield     | 3   | 2          | ₹95,00,000          |
| Indiranagar    | 2   | 3          | ₹1,10,00,000        |
| Electronic City | 1   | 1          | ₹48,00,000          |

---

## 🧠 Model Training Summary

- Algorithm: **Multiple Linear Regression**  
- Evaluation Metric: **R² Score = 0.85**  
- Dataset: **Bengaluru House Prices Dataset**  
- Preprocessing:
  - Handled missing values and outliers  
  - Used one-hot encoding for categorical variables  
  - Normalized numerical features  

---
