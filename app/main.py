import streamlit as st
from load_predict import predict

st.set_page_config(page_title="Lauki Finance", layout="wide")
st.title("Lauki Finance: Credit Risk Modelling")

left_col, mid_col, right_col = st.columns([2, 0.1, 0.9])

with left_col:
    st.subheader("Applicant Details")
    
    row1 = st.columns(4)
    row2 = st.columns(4)
    row3 = st.columns(4)

    # Input fields for user data
    with row1[0]:
        age = st.number_input('Age', min_value=18, max_value=100, value=30, step=1)
    with row1[1]:
        income = st.number_input('Income', min_value=0, value=50000)
    with row1[2]:
        loan_amount = st.number_input('Loan Amount', min_value=1000, max_value=50000000, value=150000)
    with row1[3]:
        loan_tenure_months = st.number_input('Loan Tenure Months',  min_value=6, max_value=60, step=1, value=6)

    with row2[0]:
        residence_type = st.selectbox('Residence Type', options=['Owned', 'Rented', 'Mortage'], index=0)
    with row2[1]:
        loan_purpose = st.selectbox('Loan Purpose', options=['Personal', 'Home', 'Auto', 'Education'], index=0)
    with row2[2]:
        loan_type = st.selectbox('Loan Type', options=['Secured', 'Unsecured'], index=0)
    with row2[3]:
        number_of_open_accounts = st.number_input('Number of Open Accounts', min_value=1, max_value=10, value=2, step=1)

    with row3[0]:
        credit_utilization_ratio = st.number_input('Credit Utilization Ratio', min_value=0.0, max_value=100.0, value=30.0, step=0.01)
    with row3[1]:
        delinquency_ratio = st.number_input('Delinquency Ratio', min_value=0.0, max_value=100.0, value=20.0, step=0.01)
    with row3[2]:
        avg_dpd_per_delinquency = st.number_input('Avg DPD per Delinquency', min_value=0.0, value=5.0, step=0.1)

    # Calculate loan_to_income ratio
    loan_to_income = loan_amount / income if income > 0 else 0
    with row3[3]:
        st.text(f'Loan to Income Ratio:')
        st.text(f'{loan_to_income:.2f}')
    st.markdown("") # Add spacing between the last row and the

    input_data = {
        'age': age,
        'loan_tenure_months': loan_tenure_months, 
        'number_of_open_accounts': number_of_open_accounts, 
        'credit_utilization_ratio': credit_utilization_ratio, 
        'loan_to_income': loan_to_income, 
        'delinquency_ratio': delinquency_ratio, 
        'avg_dpd_per_delinquency': avg_dpd_per_delinquency, 
        'residence_type_Owned': 1 if residence_type == 'Owned' else 0, 
        'residence_type_Rented': 1 if residence_type == 'Rented' else 0, 
        'loan_purpose_Education': 1 if loan_purpose == 'Education' else 0,	
        'loan_purpose_Home': 1 if loan_purpose == 'Home' else 0,
        'loan_purpose_Personal': 1 if loan_purpose == 'Personal' else 0,
        'loan_type_Unsecured': 1 if loan_type == 'Unsecured' else 0,
        'number_of_dependants': 1, 
        'years_at_current_address': 1,
        'sanction_amount': 1, 
        'processing_fee': 1, 
        'gst': 1, 
        'net_disbursement': 1,
        'loan_tenure_months': 1, 
        'principal_outstanding': 1,
        'bank_balance_at_application': 1, 
        'number_of_closed_accounts': 1, 
        'enquiry_count': 1
    }

    # --- Centered Predict Button ---
    col_a, col_b, col_c = st.columns([1.2, 1, 0.8])

    with col_b:
        if st.button("Calculate Credit Risk"):
            probability, credit_score, rating = predict(input_data)
            st.session_state['prediction'] = {
                "probability": probability,
                "credit_score": credit_score,
                "rating": rating
            }

# Display prediction results in the right column
with right_col:
    st.subheader("Prediction Results")
    st.markdown(" ")
    if "prediction" in st.session_state:
        st.write(f"**Probability of Default:** {st.session_state['prediction']['probability']}%")
        st.write(f"**Credit Score:** {st.session_state['prediction']['credit_score']}")
        st.write(f"**Credit Rating:** {st.session_state['prediction']['rating']}")
    else:
        st.info("Enter values and click *Calculate Credit Risk* to see prediction.")
