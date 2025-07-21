## Lauki Finance – Credit Risk Modelling App

### Predict Credit Risk with Logistic Regression

Welcome to **Lauki Finance**, a machine learning-powered application that assesses the creditworthiness of loan applicants. This project uses a **logistic regression model** to predict the **probability of default** and calculate a **credit score** (ranging from 300 to 900). Based on the score, each applicant is assigned a **credit rating**: **Poor**, **Fair**, **Good**, **Very Good**, or **Excellent**.

<br>

## Project Overview

Many financial institutions rely on credit scoring models to determine the risk of lending. This project simulates a real-world **credit risk evaluation system** by:

* Accepting applicant information (age, income, loan amount, etc.)
* Predicting the likelihood of default using a trained logistic regression model
* Generating a standardized credit score between **300–900**
* Assigning a risk rating based on the credit score

The interactive frontend is built using **Streamlit**, offering a simple interface for credit officers and loan assessors.



## Credit Score & Rating System

| Credit Score Range | Credit Rating |
|--------------------|----------------|
| 300 – 499          | Poor           |
| 500 – 649          | Fair           |
| 650 – 749          | Good           |
| 750 – 849          | Very Good      |
| 850 – 900          | Excellent      |

> These bands are inspired by conventional credit rating systems and serve as a general benchmark.



## Features

* Logistic regression model for binary classification (default vs non-default)
* Scaled input features for better model generalization
* Dynamic credit scoring logic mapped from predicted probability
* Real-time predictions via a **Streamlit web app**
* Intuitive 2-column layout with input and output separation



## Tech Stack

- Python (Logistic Regression)
- Streamlit
- Scikit-learn
- Pandas, NumPy



## App Preview

> *Insert a screenshot or GIF of the app here if available*



## Getting Started

1. Clone the repo
2. Install requirements  
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the Streamlit app
    ```bash
    cd app
    streamlit run main.py
    ```



## Project Structure

```
credit-risk-model/app
│
├── main.py                  # Main Streamlit app
├── load_predict.py         # Prediction logic and model loading
├── model/
│   └── credit_risk_model.pkl     # Serialized logistic regression model
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── ...
```



## Input Features

Some of the features used by the model:

* Age
* Income
* Loan Amount
* Loan Tenure
* Residence Type
* Loan Purpose & Type
* Credit Utilization Ratio
* Delinquency Ratio
* Average DPD per Delinquency
* Number of Open Accounts
* Loan-to-Income Ratio (calculated)
* Additional engineered/dummy features for prediction



## Credit Score Calculation Logic

The probability output by the logistic regression model is mapped to a **credit score** between 300 and 900 using a linear transformation:

```python
score = 900 - (probability_of_default * 600)
```

This ensures that lower default probabilities lead to higher credit scores.



## Future Improvements

* Model upgrade (e.g., using XGBoost or ensemble methods)
* Support for file-based batch predictions
* User authentication for internal access
* Historical prediction tracking and logs
* Integration with cloud platforms (e.g., Streamlit Cloud)



