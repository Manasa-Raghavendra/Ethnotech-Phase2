import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Pneumonia Detection",
    page_icon="🫁",
    layout="centered"
)


# --------------------------------------------------
# Load Model
# --------------------------------------------------

@st.cache_resource
def load_pneumonia_model():
    model = tf.keras.models.load_model(
        "vgg16_pneumonia_final.keras"
    )
    return model


model = load_pneumonia_model()


# --------------------------------------------------
# Preprocess Image
# --------------------------------------------------

def preprocess_image(image):
    # Convert image to RGB
    image = image.convert("RGB")

    # Resize to VGG16 input size
    image = image.resize((224, 224))

    # Convert to NumPy array
    image_array = np.array(image)

    # Normalize pixel values
    image_array = image_array / 255.0

    # Add batch dimension
    image_array = np.expand_dims(image_array, axis=0)

    return image_array


# --------------------------------------------------
# Prediction Function
# --------------------------------------------------

def predict_pneumonia(image):
    processed_image = preprocess_image(image)

    prediction = model.predict(
        processed_image,
        verbose=0
    )

    probability = float(prediction[0][0])

    if probability >= 0.5:
        predicted_class = "PNEUMONIA"
        confidence = probability
    else:
        predicted_class = "NORMAL"
        confidence = 1 - probability

    return predicted_class, confidence, probability


# --------------------------------------------------
# User Interface
# --------------------------------------------------

st.title("🫁 Pneumonia Detection using VGG16")

st.write(
    "Upload a chest X-ray image and the trained VGG16 "
    "model will predict whether the image is Normal or Pneumonia."
)


# --------------------------------------------------
# File Uploader
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload a Chest X-ray image",
    type=["jpg", "jpeg", "png"]
)


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("Uploaded X-ray")

    st.image(
        image,
        caption="Chest X-ray",
        use_container_width=True
    )

    if st.button("🔍 Predict Pneumonia"):

        with st.spinner("Analyzing X-ray..."):

            predicted_class, confidence, probability = (
                predict_pneumonia(image)
            )

        st.subheader("Prediction")

        if predicted_class == "PNEUMONIA":

            st.error(
                f"🫁 Prediction: PNEUMONIA"
            )

            st.write(
                f"Confidence: {confidence * 100:.2f}%"
            )

        else:

            st.success(
                f"✅ Prediction: NORMAL"
            )

            st.write(
                f"Confidence: {confidence * 100:.2f}%"
            )

        # Show raw model probability
        st.write(
            f"Pneumonia probability: "
            f"{probability * 100:.2f}%"
        )


# --------------------------------------------------
# Information Section
# --------------------------------------------------

st.divider()

st.subheader("About the Model")

st.write(
    """
    This application uses a VGG16 convolutional neural network
    with transfer learning for binary chest X-ray classification.

    The model was trained to classify images into:

    • NORMAL
    • PNEUMONIA

    Input images are resized to 224 × 224 pixels and converted
    to RGB format before prediction.
    """
)

st.warning(
    "This application is intended for educational and "
    "demonstration purposes only and should not be used "
    "as a substitute for professional medical diagnosis."
)