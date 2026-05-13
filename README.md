# Customer Churn Prediction Dashboard

A Machine Learning-powered Customer Churn Prediction Dashboard built using Python, Streamlit, and XGBoost.
This project predicts whether a customer is likely to churn based on service usage, billing information, and customer behavior.

---

## Features

* Interactive Streamlit Dashboard
* Real-time Customer Churn Prediction
* Churn Probability Score
* User-friendly Interface
* Machine Learning Model Integration
* Customer Summary Display

---

## Tech Stack

* Python
* Streamlit
* Pandas
* Scikit-learn
* XGBoost
* Pickle

---

## Dataset

Dataset Used: IBM Telco Customer Churn Dataset

The dataset contains:

* Customer demographics
* Billing information
* Internet services
* Contract details
* Support services
* Churn status

---

## Project Structure

```bash
customer-churn-prediction/
│
├── app.py
├── requirements.txt
├── README.md
├── model.pkl
├── model_columns.pkl
│
├── data/
│   └── telco_customer_churn.xlsx
│
├── notebooks/
│   └── model_training.ipynb
│
├── screenshots/
│   └── dashboard.png
│
└── .gitignore
```

---

## Installation & Setup

### Clone Repository

```bash
git clone https://github.com/yourusername/customer-churn-prediction.git
```

### Navigate to Project Folder

```bash
cd customer-churn-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

---

## Dashboard Preview

(Add your project screenshot here)

Example:

```markdown
![Dashboard Screenshot](screenshots/dashboard.png)
```

---

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Feature Encoding
4. Model Training using XGBoost
5. Model Serialization using Pickle
6. Streamlit Dashboard Deployment

---

## Prediction Features

The model uses the following features for prediction:

* Tenure Months
* Monthly Charges
* Contract Type
* Internet Service
* Payment Method
* Tech Support
* Online Security
* Paperless Billing
* Senior Citizen

---

## Future Improvements

* Add Data Visualization Charts
* Bulk CSV Prediction
* Feature Importance Visualization
* Dark Mode UI
* Deploy on Streamlit Cloud
* Add Authentication System

---

## Author

Ritik Roushan
Data Analyst & Machine Learning Enthusiast

---

## License

This project is open-source and available under the MIT License.
