import streamlit as st
import pandas as pd
from xgboost import XGBClassifier


# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="🏦",
    layout="wide"
)


# ---------------------------------------------------
# LOAD TRAINED MODEL
# ---------------------------------------------------

model = XGBClassifier()
model.load_model("churn_model.json")


# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: #1f4e79;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555555;
    margin-bottom: 30px;
}

.card {
    padding: 25px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.result-box {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.markdown(
    '<div class="title">🏦 Customer Churn Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict whether a bank customer is likely to leave the bank using Machine Learning</div>',
    unsafe_allow_html=True
)

st.divider()


# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.header("📌 About the Model")

    st.write(
        """
        This application uses an **XGBoost Machine Learning model**
        to predict customer churn.
        """
    )

    st.write("### Model Information")

    st.info(
        """
        **Algorithm:** XGBoost

        **Maximum Depth:** 3

        **Test Accuracy:** 87.05%
        """
    )

    st.write("### Prediction Classes")

    st.success("0 → Customer likely to stay")

    st.error("1 → Customer likely to churn")


# ---------------------------------------------------
# CUSTOMER INFORMATION
# ---------------------------------------------------

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.subheader("👤 Customer Information")

col1, col2, col3 = st.columns(3)


# ---------------------------------------------------
# COLUMN 1
# ---------------------------------------------------

with col1:

    customer_id = st.number_input(
        "Customer ID",
        min_value=1,
        value=100000,
        step=1
    )

    credit_score = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=900,
        value=650,
        step=1
    )

    geography = st.selectbox(
        "Geography",
        ["France", "Germany", "Spain"]
    )

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )


# ---------------------------------------------------
# COLUMN 2
# ---------------------------------------------------

with col2:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=35,
        step=1
    )

    tenure = st.number_input(
        "Tenure (Years)",
        min_value=0,
        max_value=10,
        value=5,
        step=1
    )

    balance = st.number_input(
        "Account Balance",
        min_value=0.0,
        value=50000.0,
        step=1000.0
    )

    estimated_salary = st.number_input(
        "Estimated Salary",
        min_value=0.0,
        value=50000.0,
        step=1000.0
    )


# ---------------------------------------------------
# COLUMN 3
# ---------------------------------------------------

with col3:

    num_products = st.number_input(
        "Number of Products",
        min_value=1,
        max_value=4,
        value=1,
        step=1
    )

    has_card = st.selectbox(
        "Has Credit Card?",
        ["Yes", "No"]
    )

    active_member = st.selectbox(
        "Is Active Member?",
        ["Yes", "No"]
    )


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------
# PREDICTION BUTTON
# ---------------------------------------------------

st.write("")

predict_button = st.button(
    "🔍 Predict Customer Churn",
    use_container_width=True
)


# ---------------------------------------------------
# PREDICTION
# ---------------------------------------------------

if predict_button:

    # -----------------------------------------------
    # ENCODE CATEGORICAL FEATURES
    # -----------------------------------------------

    if geography == "France":
        geography_encoded = 0

    elif geography == "Germany":
        geography_encoded = 1

    else:
        geography_encoded = 2


    if gender == "Female":
        gender_encoded = 0

    else:
        gender_encoded = 1


    if has_card == "Yes":
        has_card_encoded = 1

    else:
        has_card_encoded = 0


    if active_member == "Yes":
        active_member_encoded = 1

    else:
        active_member_encoded = 0


    # -----------------------------------------------
    # CREATE INPUT DATA
    # -----------------------------------------------

    input_data = pd.DataFrame({

        "CustomerId": [customer_id],

        "CreditScore": [credit_score],

        "Geography": [geography_encoded],

        "Gender": [gender_encoded],

        "Age": [age],

        "Tenure": [tenure],

        "Balance": [balance],

        "NumOfProducts": [num_products],

        "HasCrCard": [has_card_encoded],

        "IsActiveMember": [active_member_encoded],

        "EstimatedSalary": [estimated_salary]

    })


    # -----------------------------------------------
    # MAKE PREDICTION
    # -----------------------------------------------

    prediction = model.predict(input_data)

    probability = model.predict_proba(input_data)

    churn_probability = probability[0][1] * 100

    stay_probability = probability[0][0] * 100


    # -----------------------------------------------
    # DISPLAY RESULT
    # -----------------------------------------------

    st.divider()

    st.subheader("📊 Prediction Result")


    # -----------------------------------------------
    # CUSTOMER LIKELY TO CHURN
    # -----------------------------------------------

    if prediction[0] == 1:

        st.error(
            "⚠️ The customer is likely to churn."
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Churn Probability",
                f"{churn_probability:.2f}%"
            )

        with col2:

            st.metric(
                "Stay Probability",
                f"{stay_probability:.2f}%"
            )

        st.warning(
            "This customer may be at risk of leaving the bank. "
            "The bank can consider providing personalized offers "
            "or customer retention services."
        )


    # -----------------------------------------------
    # CUSTOMER LIKELY TO STAY
    # -----------------------------------------------

    else:

        st.success(
            "✅ The customer is likely to stay."
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Stay Probability",
                f"{stay_probability:.2f}%"
            )

        with col2:

            st.metric(
                "Churn Probability",
                f"{churn_probability:.2f}%"
            )

        st.success(
            "This customer appears to have a lower risk of leaving "
            "the bank based on the model prediction."
        )


    # -----------------------------------------------
    # PROBABILITY BAR
    # -----------------------------------------------

    st.subheader("📈 Churn Probability")

    st.progress(
        int(churn_probability)
    )


    # -----------------------------------------------
    # SHOW INPUT DATA
    # -----------------------------------------------

    with st.expander("🔎 View Customer Data Used for Prediction"):

        st.dataframe(
            input_data,
            use_container_width=True
        )