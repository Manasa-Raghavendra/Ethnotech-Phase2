import numpy as np
import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, "model", "sequence_map.pkl"), "rb") as f:
    sequence_map = pickle.load(f)

with open(os.path.join(BASE_DIR, "model", "structure_map.pkl"), "rb") as f:
    structure_map = pickle.load(f)

with open(os.path.join(BASE_DIR, "model", "loop_map.pkl"), "rb") as f:
    loop_map = pickle.load(f)


# ------------------------------------------
# Encode helper
# ------------------------------------------

def encode(text, mapping):
    return [mapping[c] for c in text]


# ------------------------------------------
# Pad / Crop helper
# ------------------------------------------

def fix_length(values, target_length=107):
    """
    Make every sequence exactly 107 long.
    """

    if len(values) > target_length:
        return values[:target_length]

    if len(values) < target_length:
        return values + [0] * (target_length - len(values))

    return values


# ------------------------------------------
# Main preprocessing
# ------------------------------------------

def preprocess_dataframe(df):

    seq = [
        fix_length(encode(x, sequence_map))
        for x in df["sequence"]
    ]

    struct = [
        fix_length(encode(x, structure_map))
        for x in df["structure"]
    ]

    loop = [
        fix_length(encode(x, loop_map))
        for x in df["predicted_loop_type"]
    ]

    X_seq = np.array(seq, dtype=np.int32)
    X_struct = np.array(struct, dtype=np.int32)
    X_loop = np.array(loop, dtype=np.int32)

    return X_seq, X_struct, X_loop