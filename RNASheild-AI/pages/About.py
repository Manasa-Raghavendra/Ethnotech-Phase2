import streamlit as st

st.title("📖 About Project")

st.header("Project Title")

st.write("""
Explainable Deep Learning Platform
for COVID-19 mRNA Stability Prediction
""")

st.header("Objective")

st.write("""
Predict degradation of RNA molecules under
different environmental conditions using
Deep Learning.
""")

st.header("Model")

st.write("""
Bi-directional LSTM

Embedding Layers

TimeDistributed Dense Layer

TensorFlow / Keras
""")

st.header("Dataset")

st.write("""
COVID-19 mRNA Vaccine Degradation Dataset

Train Samples: 2400

Sequence Length: 107

Predicted Positions: 68
""")