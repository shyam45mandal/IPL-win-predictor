# 🏏 IPL Win Percentage Predictor

A **Streamlit web app** that predicts the win percentage of two IPL teams based on the current match situation using a Machine Learning model trained in Python.

---

## 📖 How This Project Was Made

### **1. Data Collection**
- Collected IPL match data from Kaggle.
- Loaded it into **Pandas DataFrames** for analysis.

### **2. Data Preprocessing (in Jupyter Notebook)**
- Handled missing values.
- Encoded categorical variables (teams, city, toss decision).
- Created new features:
  - `runs_left` = target - current score
  - `balls_left` = 120 - overs_completed × 6
  - `wickets_left` = 10 - wickets_fallen
  - `crr` = current run rate
  - `rrr` = required run rate
- Split data into train and test sets.

### **3. Model Training**
- Used **Logistic Regression / Random Forest** from `scikit-learn`.
- Trained on historical IPL match data.
- Evaluated with **accuracy** and **confusion matrix**.

### **4. Saving the Model**
- Saved the trained model as a `.pkl` file using `pickle`:
```python
import pickle
pickle.dump(model, open('model.pkl', 'wb'))
