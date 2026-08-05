# ==========================================
# app.py
# RNAShield AI
# ==========================================

import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="RNAShield AI",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown("""
<style>

.main{
    padding-top:20px;
}

.big-font{
    font-size:42px;
    font-weight:bold;
    color:#1565C0;
}

.subtitle{
    font-size:20px;
    color:gray;
}

.feature{
    background-color:#F8F9FA;
    padding:20px;
    border-radius:12px;
    margin-bottom:15px;
    box-shadow:2px 2px 8px rgba(0,0,0,0.08);
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("🧬 RNAShield AI")

st.sidebar.success(
"""
Navigation

🏠 Home

🤖 Predict

📊 Analytics

📖 About

❓ Help
"""
)

st.sidebar.info(
"""
Select a page from the sidebar
to begin.
"""
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
'<p class="big-font">🧬 RNAShield AI</p>',
unsafe_allow_html=True
)

st.markdown(
'<p class="subtitle">'
'Explainable Deep Learning Platform for COVID-19 mRNA Stability Prediction'
'</p>',
unsafe_allow_html=True
)

st.markdown("---")

# --------------------------------------------------
# Introduction
# --------------------------------------------------

st.header("Welcome")

st.write("""
RNAShield AI is an AI-powered platform developed to analyze the
stability of COVID-19 mRNA molecules.

The application predicts how different regions of an RNA molecule
behave under different environmental conditions such as:

- High pH
- High Temperature (50°C)
- Magnesium Environment

The platform also explains the predictions in simple language,
making the results understandable for both technical and
non-technical users.
""")

# --------------------------------------------------
# Features
# --------------------------------------------------

st.markdown("---")

st.header("✨ Key Features")

col1, col2, col3 = st.columns(3)

with col1:

    st.info("""
🧬 Deep Learning Prediction

Predict degradation using
a trained Bi-LSTM model.
""")

with col2:

    st.info("""
📊 Interactive Visualizations

Line Charts

Heatmaps

Health Score
""")

with col3:

    st.info("""
🧠 Explainable AI

Simple language interpretation

Easy-to-understand results
""")

# --------------------------------------------------
# Workflow
# --------------------------------------------------

st.markdown("---")

st.header("🔄 Workflow")

st.write("""

Upload RNA JSON

⬇️

Preprocessing

⬇️

Deep Learning Prediction

⬇️

AI Interpretation

⬇️

Interactive Dashboard

⬇️

Download Report

""")

# --------------------------------------------------
# Technology Stack
# --------------------------------------------------

st.markdown("---")

st.header("💻 Technology Stack")

tech1, tech2 = st.columns(2)

with tech1:

    st.success("Python")

    st.success("TensorFlow")

    st.success("Keras")

    st.success("NumPy")

with tech2:

    st.success("Pandas")

    st.success("Plotly")

    st.success("Streamlit")

    st.success("Deep Learning (Bi-LSTM)")

# --------------------------------------------------
# Dataset Information
# --------------------------------------------------

st.markdown("---")

st.header("📂 Dataset")

st.write("""

Dataset : COVID-19 mRNA Vaccine Degradation Dataset

Training Samples : 2400

Sequence Length : 107

Prediction Length : 68 Positions

Prediction Outputs : 5

• Reactivity

• deg_pH10

• deg_Mg_pH10

• deg_50C

• deg_Mg_50C

""")

# --------------------------------------------------
# Quick Start
# --------------------------------------------------

st.markdown("---")

st.header("🚀 Quick Start")

st.write("""

1️⃣ Open **Predict** page

2️⃣ Upload **test.json**

3️⃣ Select RNA Molecule

4️⃣ Click **Predict**

5️⃣ View Dashboard

6️⃣ Interpret Results

7️⃣ Download Report

""")

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.markdown(
"""
<div class="footer">

Developed as a Deep Learning Project

<b>RNAShield AI</b><br>

Explainable Deep Learning Platform for COVID-19 mRNA Stability Prediction

</div>
""",
unsafe_allow_html=True
)