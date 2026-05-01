# fraud-detection-ml
# 💳 Credit Card Fraud Detection System

A Machine Learning project that detects fraudulent credit card transactions using **Logistic Regression**, with a complete pipeline and a simple **Streamlit web app** for real-time predictions.

---

## 🚀 Project Overview

This project aims to identify fraudulent transactions from credit card data using supervised machine learning.
It uses a well-structured ML pipeline with preprocessing and model training to achieve high accuracy.

✅ Model Accuracy: **~94%**

---

## 🧠 Technologies Used

* Python 🐍
* Scikit-learn
* Pandas & NumPy
* Joblib (for model saving/loading)
* Streamlit (for web app)

---

## ⚙️ Features

* Data preprocessing using **ColumnTransformer**
* ML Pipeline for clean and scalable workflow
* Logistic Regression model
* Model serialization using Joblib
* Interactive web app using Streamlit
* Real-time fraud prediction

---

## 📂 Project Structure

```
📁 Fraud Detection Project
│── Fraud_detection.py        # Main application (Streamlit app)
│── analysis_model.ipynb      # Model training & analysis
│── .gitignore
│── README.md
```

---

## 🧪 Model Details

* Algorithm: **Logistic Regression**
* Pipeline:

  * Data Cleaning
  * Feature Transformation (ColumnTransformer)
  * Model Training
* Performance:

  * Accuracy: **94%**

---

## 🌐 Streamlit App

This project includes a simple UI built with Streamlit where users can input transaction details and get predictions instantly.

### ▶️ Run the app locally:

```bash
streamlit run Fraud_detection.py
```

---

## 📊 Dataset

Due to GitHub file size limits, the dataset is not included in this repository.

👉 Add your dataset here:

```
https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset
```

Or use your own dataset with the same structure.

---

## 💾 Model File

The trained model (`.pkl`) is not uploaded due to size limitations.

To generate it:

1. Run the Jupyter Notebook
2. Save model using Joblib

---

## 📌 Future Improvements

* Use advanced models (Random Forest, XGBoost)
* Improve accuracy & reduce false positives
* Deploy app on cloud (Streamlit Cloud / AWS)
* Add user authentication

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Subhransu Dhar**

---

⭐ If you like this project, give it a star on GitHub!
