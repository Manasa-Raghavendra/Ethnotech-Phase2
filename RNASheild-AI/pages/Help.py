import streamlit as st

st.title("❓ Help")

st.header("How to Use")

st.write("""
Step 1

Open Predict Page

Step 2

Upload test.json

Step 3

Select RNA Molecule

Step 4

Click Predict

Step 5

View Dashboard
""")

st.header("Meaning of Predictions")

st.write("""
Reactivity

Shows structural flexibility.

Higher values indicate increased flexibility.

deg_pH10

Likelihood of degradation in alkaline conditions.

deg_Mg_pH10

Degradation in alkaline conditions
when Magnesium is present.

deg_50C

Thermal degradation at 50°C.

deg_Mg_50C

Thermal degradation at 50°C
with Magnesium.
""")