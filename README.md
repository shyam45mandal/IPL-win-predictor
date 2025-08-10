# 🏏 IPL Win Predictor

A machine learning-powered web application built with **Streamlit** that predicts the winning probability of IPL teams based on live match details such as batting team, bowling team, target, and current score.

🔗 **Live App:** [IPL Win Predictor](https://ipl-win-predictor-dcqchja92nz9tusrquvzgb.streamlit.app/)

---

## 🚀 Features

- Predict winning probability in real time
- User-friendly **Streamlit** interface
- Uses IPL match data for training
- Takes into account current score, overs, wickets, and target
- Deployed on **Streamlit Cloud**

---

## 📊 How It Works

1. **Data Preparation** – IPL historical data is cleaned and preprocessed  
2. **Feature Engineering** – Extract relevant match stats (run rate, wickets left, etc.)  
3. **Model Training** – A machine learning model predicts probabilities for both teams  
4. **Web App** – Model integrated with Streamlit for easy interaction  

---

## 🛠️ Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Streamlit**
- **Matplotlib / Seaborn** (for data visualization)

---
IPL_PREDICTION/
│
├── app.py # Main Streamlit app (entry point)
├── model.pkl # Trained machine learning model file
├── requirements.txt # Python dependencies required for the project
├── README.md # Project documentation
└── data/ # Dataset folder containing IPL match data
├── ipl_dataset.csv # Processed/cleaned dataset
└── raw/ # (Optional) Raw IPL data before preprocessing



--



## 📂 Project Structure

