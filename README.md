# 🛡️ CreditShield AI: Advanced Financial Risk Terminal

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg.svg)](YOUR_DEPLOYED_APP_LINK_HERE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**CreditShield AI** is a professional-grade machine learning application designed to predict loan default risks. Built using a **Decision Tree Classifier**, the system analyzes applicant profiles (income, employment length, credit history) to provide real-time eligibility verdicts with high explainability.

---

## 🚀 Live Demo
**Check out the live app here:** [CreditShield AI Terminal](YOUR_DEPLOYED_APP_LINK_HERE)

---

## 🧠 Model Intelligence
The "brain" of this project is a Decision Tree model trained on a comprehensive credit risk dataset.
* **Accuracy:** ~92%
* **Key Features:** Entropy-based splitting, handling of class imbalance, and outlier removal (addressing unrealistic age/employment data).
* **Explainable AI (XAI):** Unlike "black-box" models, this system provides a clear decision path, making it ideal for the highly regulated financial sector.



---

## ✨ Key Features
* **Modern UI/UX:** Built with a Glassmorphism design, Lottie animations, and custom CSS styling.
* **Interactive Visuals:** Uses Plotly Gauge Charts to represent model confidence levels visually.
* **Real-time Inference:** Fast prediction engine with automated feature encoding.
* **Responsive Design:** Optimized for both desktop and mobile viewing.

---

## 🛠️ Tech Stack
* **Language:** Python
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Frontend/UI:** Streamlit, Streamlit-Lottie
* **Visualization:** Plotly
* **Deployment:** Streamlit Cloud / GitHub

---

## 📂 Project Structure
```text
├── app.py              # Main Streamlit application
├── model_training.ipynb # Jupyter Notebook (Model Development)
├── model.pkl           # Trained Decision Tree model
├── mappings.pkl        # Categorical encoding mappings
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation