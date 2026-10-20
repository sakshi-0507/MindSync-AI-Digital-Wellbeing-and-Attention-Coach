# 🧠 MindSync AI

**Your Personalized Digital Wellbeing and Attention Coach**

MindSync AI is a Streamlit web app that uses a trained machine-learning model to estimate a person's digital-habit risk category (**Low / Medium / High**) from 20 lifestyle and phone-usage inputs, then gives practical suggestions to build healthier routines.

## ✨ Features

- **Risk prediction** with probability scores
- **Personalized suggestions** (rule-based)
- **What-If Habit Simulator** to compare current vs. adjusted habits
- **Digital Attention Budget** to set a daily phone-use goal
- **7-Day Wellbeing Coach** with a progress tracker
- **Progress Dashboard** with charts
- **Offline chatbot**, with no API key or external AI service

## 🛠️ Tech Stack

Python · Streamlit · scikit-learn (Random Forest) · pandas · joblib

## 📁 Project Structure

```
├── app.py                          # Streamlit application
├── requirements.txt                # Dependencies
├── mindsync_models/
│   └── mindsync_model_bundle.joblib  # Trained model, scaler, features
└── AI-Based_Social_Media_Information_Overload_Prediction.ipynb  # Model training
```

## 🚀 Run Locally

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python -m venv venv
venv\Scripts\activate          # Windows  (Linux/Mac: source venv/bin/activate)
pip install -r requirements.txt
streamlit run app.py
```

Open http://localhost:8501

## ☁️ Deploy on AWS (EC2)

1. Launch an **Ubuntu 24.04** EC2 instance (`t3.small` recommended).
2. Open **port 8501** in the security group.
3. Install Python and Git, clone this repo, then install the requirements.
4. Run:
   ```bash
   streamlit run app.py --server.port 8501 --server.address 0.0.0.0
   ```
5. Visit `http://<EC2-PUBLIC-IP>:8501`

> Use the **same scikit-learn version** on the server as the one used to train the model.

## ⚠️ Disclaimer

MindSync AI gives model-based estimates and general habit suggestions. It is **not** a medical or psychological diagnosis or advice.

## 📄 Dataset

Trained on the *Teen Phone Addiction* dataset.
