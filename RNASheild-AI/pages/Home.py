import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

st.title("🧬 Welcome to RNAShield AI")

st.markdown("---")

st.header("What is RNAShield AI?")

st.write("""
RNAShield AI is an Explainable Deep Learning platform developed to
predict the degradation behaviour of COVID-19 mRNA molecules.

The application analyses RNA sequences and estimates how stable
different regions of the molecule remain under various environmental
conditions such as:

• High pH

• High Temperature (50°C)

• Presence of Magnesium ions

The goal is to assist researchers in identifying unstable regions
that may affect vaccine stability.
""")

st.markdown("---")

st.header("Why is this Important?")

st.write("""
mRNA molecules are naturally fragile.

If degradation occurs:

✔ Vaccine effectiveness decreases

✔ Storage becomes difficult

✔ Transportation requires strict cold-chain conditions

Predicting unstable regions helps scientists design
more stable mRNA vaccines.
""")

st.markdown("---")

st.header("Features")

col1, col2 = st.columns(2)

with col1:

    st.success("🧬 Deep Learning Prediction")

    st.success("📈 Interactive Graphs")

    st.success("🔥 Heatmaps")

with col2:

    st.success("🧠 AI Interpretation")

    st.success("📄 Download Reports")

    st.success("📊 Analytics Dashboard")

st.markdown("---")

st.header("Technology Stack")

st.write("""
• Python

• TensorFlow / Keras

• Streamlit

• Plotly

• Pandas

• NumPy

• Deep Learning (Bi-LSTM)
""")