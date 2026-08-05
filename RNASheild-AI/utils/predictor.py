# ==========================================
# predictor.py
# ==========================================

import os
import pickle
import numpy as np
import tensorflow as tf
import keras

# --------------------------------------------------
# Enable loading of Lambda layer (Keras 3.x)
# --------------------------------------------------

keras.config.enable_unsafe_deserialization()

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "model", "rna_model.keras")

SEQ_MAP_PATH = os.path.join(BASE_DIR, "model", "sequence_map.pkl")

STRUCT_MAP_PATH = os.path.join(BASE_DIR, "model", "structure_map.pkl")

LOOP_MAP_PATH = os.path.join(BASE_DIR, "model", "loop_map.pkl")

# --------------------------------------------------
# Load Model
# --------------------------------------------------

try:

    model = tf.keras.models.load_model(
        MODEL_PATH,
        safe_mode=False
    )

    print("✅ RNA Model Loaded Successfully")

except Exception as e:

    print("❌ Error Loading Model")

    print(e)

    model = None

# --------------------------------------------------
# Load Encoding Dictionaries
# --------------------------------------------------

with open(SEQ_MAP_PATH, "rb") as f:
    sequence_map = pickle.load(f)

with open(STRUCT_MAP_PATH, "rb") as f:
    structure_map = pickle.load(f)

with open(LOOP_MAP_PATH, "rb") as f:
    loop_map = pickle.load(f)

# --------------------------------------------------
# Prediction Function
# --------------------------------------------------

def predict(X_seq, X_struct, X_loop):
    """
    Predict degradation values.

    Parameters
    ----------
    X_seq : numpy.ndarray
        Encoded RNA sequences

    X_struct : numpy.ndarray
        Encoded RNA structures

    X_loop : numpy.ndarray
        Encoded loop types

    Returns
    -------
    numpy.ndarray
        Shape:
        (samples, 68, 5)
    """

    if model is None:
        raise ValueError("Model could not be loaded.")

    predictions = model.predict(

        [

            X_seq,

            X_struct,

            X_loop

        ],

        verbose=0

    )

    return predictions

# --------------------------------------------------
# Predict Single RNA
# --------------------------------------------------

def predict_single(sequence, structure, loop_type):
    """
    Predict a single RNA molecule.

    Parameters
    ----------
    sequence : str
    structure : str
    loop_type : str

    Returns
    -------
    ndarray (68,5)
    """

    seq = np.array([[sequence_map[c] for c in sequence]])

    struct = np.array([[structure_map[c] for c in structure]])

    loop = np.array([[loop_map[c] for c in loop_type]])

    prediction = predict(seq, struct, loop)

    return prediction[0]