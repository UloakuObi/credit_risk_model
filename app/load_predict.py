# This file handles model loading and prediction.
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


model_path = 'app/model/credit_risk_model.joblib'
model_data = joblib.load(model_path)
model = model_data['model']
scaler = model_data['scaler']
features = model_data['features']
cols_to_scale = model_data['cols_to_scale']


# Define the expected features for the model
expected_features = ['age', 'loan_tenure_months', 'number_of_open_accounts', 'credit_utilization_ratio', 'loan_to_income', 
            'delinquency_ratio', 'avg_dpd_per_delinquency', 'residence_type_Owned', 'residence_type_Rented', 
            'loan_purpose_Education',	'loan_purpose_Home', 'loan_purpose_Personal', 'loan_type_Unsecured']

def preprocess_data(input_data):
    # Create a dataframe with input data
    df = pd.DataFrame([input_data]) # OR df = pd.DataFrame([input_data])

    # Scaler the appropriate columns
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])

    # Reduce the dataframe to expected features
    data = df[features].copy()
    return data

def calculate_credit_score(input_df, base_score=300, scale_length=600):

    x = np.dot(input_df, model.coef_.T) + model.intercept_
    default_probability = 1 / (1 + np.exp(-x))  # Sigmoid function
    non_default_probability = 1 - default_probability
    credit_score = base_score + (scale_length * non_default_probability.flatten())

    def get_rating(score):
        if 300 <= score < 500:
            return 'Poor'
        elif 500 <= score < 650:
            return 'Fair'
        elif 650 <= score < 750:
            return 'Good'
        elif 750 <= score < 850:
            return 'Very Good'
        elif 850 <= score <= 900:
            return 'Excellent'
        else:
            return 'Undefined' # Handle unexpected scores
        
    rating = get_rating(credit_score)
    
    return default_probability.flatten(), int(credit_score), rating


def predict(input_data):

    # Load and preprocess the input data
    input_df = preprocess_data(input_data)

    probability, credit_score, rating = calculate_credit_score(input_df)

    # Convert probability to percentage
    probability = (probability * 100).round(2)

    return probability[0], credit_score, rating
