# 💳 Fraud Detection ML System

An end-to-end **Machine Learning-based Credit Card Fraud Detection System** built using **Python, Scikit-learn, and Streamlit** to identify fraudulent financial transactions in real time.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

## 📌 Overview

Financial fraud is one of the biggest challenges in digital transactions.

This project leverages **Machine Learning classification techniques** to detect fraudulent transactions by analyzing transaction patterns and behavioral features.

The system includes:

✅ Data preprocessing pipeline  
✅ Model training and evaluation  
✅ Fraud prediction engine  
✅ Interactive Streamlit web application  
✅ Real-time transaction classification

---

## 🚀 Key Highlights

- Built complete ML pipeline using **Scikit-learn**
- Handles **imbalanced fraud detection dataset**
- Real-time prediction through Streamlit UI
- Efficient preprocessing with **ColumnTransformer**
- Model persistence using **Joblib**
- End-to-end deployment-ready structure

---

## 🧠 Tech Stack

### Programming
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Matplotlib / Seaborn
- Streamlit

### Tools
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## 📊 Model Performance

| Metric | Score |
|-------|------|
| Accuracy | **94%** |
| Precision | High |
| Recall | High |
| F1 Score | Optimized |

> The model is designed to minimize false negatives, which is critical in fraud detection systems.

---

## ⚙️ ML Workflow

```text
Raw Dataset
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Preprocessing
(ColumnTransformer)
   ↓
Train-Test Split
   ↓
Model Training
(Logistic Regression / Random Forest)
   ↓
Evaluation
   ↓
Model Saving
   ↓
Streamlit Deployment
```

---

## 📂 Project Structure

```bash
fraud-detection-ml/
│
├── Fraud_detection.py        # Streamlit web application
├── analysis_model.ipynb      # Data analysis & model training
├── model.pkl                # Saved trained model
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🌐 Streamlit Web App

The project includes an interactive web app for real-time fraud prediction.

### Run Locally

```bash
streamlit run Fraud_detection.py
```

Then open:

```bash
http://localhost:8501
```

---

## 📷 Features of Web App

✔ User-friendly interface  
✔ Manual transaction input  
✔ Instant fraud prediction  
✔ Real-time classification results

---

## 📊 Dataset

Dataset used for training:

**Credit Card Fraud Detection Dataset**

Download from Kaggle:

https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset

---

## 💾 Generate Model File

To create the trained model:

### Step 1
Run notebook:

```bash
analysis_model.ipynb
```

### Step 2
Export model using Joblib:

```python
import joblib
joblib.dump(model, "model.pkl")
```

---

## 🔮 Future Enhancements

- Implement **XGBoost / LightGBM**
- Hyperparameter optimization
- Reduce false positives
- Cloud deployment
- Dashboard analytics
- REST API integration

---

## 🤝 Contribution

Contributions are welcome.

1. Fork the repository
2. Create feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push and create Pull Request

---

## 📜 License

This project is licensed under the **MIT License**

---

## 👨‍💻 Author

### **Subhransu Dhar**

AI / ML Enthusiast  
B.Tech Student  
Passionate about Machine Learning & Deep Learning

---

## ⭐ Support

If you found this project useful:

🌟 Star this repository  
🍴 Fork it  
📢 Share it

---

### “Detecting fraud before it happens with Machine Learning.”
