import streamlit as st
import pandas as pd

from utils.preprocessing import preprocess_dataframe
from utils.predictor import predict
from utils.interpreter import interpret_prediction
from utils.visualization import (
    plot_degradation,
    plot_heatmap,
    plot_average_scores,
    plot_health_score
)

st.title("🤖 RNA Prediction")

uploaded_file = st.file_uploader(
    "Upload test.json",
    type=["json"]
)

if uploaded_file:

    test_df = pd.read_json(uploaded_file, lines=True)

    st.success("Dataset Loaded Successfully")

    selected = st.selectbox(
        "Select RNA Molecule",
        range(len(test_df)),
        format_func=lambda x: test_df.iloc[x]["id"]
    )

    if st.button("Predict"):

        X_seq, X_struct, X_loop = preprocess_dataframe(test_df)

        predictions = predict(
            X_seq,
            X_struct,
            X_loop
        )

        prediction = predictions[selected]

        average_prediction = prediction.mean(axis=0)

        st.success("Prediction Completed")

        interpretation = interpret_prediction(average_prediction)

        st.subheader("🧠 AI Interpretation")

        for key, value in interpretation.items():

            st.write(f"### {key}")

            st.success(value[0])

            st.write(value[1])

        st.plotly_chart(
            plot_degradation(prediction),
            use_container_width=True
        )

        st.plotly_chart(
            plot_heatmap(prediction),
            use_container_width=True
        )

        st.plotly_chart(
            plot_average_scores(average_prediction),
            use_container_width=True
        )

        score = max(
            0,
            100 - average_prediction[1:].mean() * 25
        )

        st.plotly_chart(
            plot_health_score(score),
            use_container_width=True
        )