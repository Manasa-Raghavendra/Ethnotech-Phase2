# ==========================================
# interpreter.py
# ==========================================

def interpret_prediction(values):

    reactivity = values[0]
    deg_pH10 = values[1]
    deg_Mg_pH10 = values[2]
    deg_50C = values[3]
    deg_Mg_50C = values[4]

    interpretation = {}

    # Reactivity
    if reactivity < 0.5:
        interpretation["Reactivity"] = (
            "🟢 Low Reactivity",
            "The RNA structure is relatively rigid and stable."
        )
    elif reactivity < 1.5:
        interpretation["Reactivity"] = (
            "🟡 Moderate Reactivity",
            "The RNA has balanced structural flexibility."
        )
    else:
        interpretation["Reactivity"] = (
            "🔴 High Reactivity",
            "The RNA is highly flexible and may be structurally unstable."
        )

    # pH10
    if deg_pH10 < 1:
        interpretation["High pH"] = (
            "🟢 Low Degradation",
            "RNA is stable under alkaline conditions."
        )
    elif deg_pH10 < 2:
        interpretation["High pH"] = (
            "🟡 Moderate Degradation",
            "Some degradation may occur at high pH."
        )
    else:
        interpretation["High pH"] = (
            "🔴 High Degradation",
            "RNA is vulnerable under alkaline conditions."
        )

    # Magnesium + pH10
    if deg_Mg_pH10 < 1:
        interpretation["Mg + High pH"] = (
            "🟢 Stable",
            "Magnesium helps maintain RNA stability."
        )
    elif deg_Mg_pH10 < 2:
        interpretation["Mg + High pH"] = (
            "🟡 Moderate Stability",
            "Magnesium provides partial protection."
        )
    else:
        interpretation["Mg + High pH"] = (
            "🔴 Unstable",
            "Magnesium is insufficient to prevent degradation."
        )

    # 50°C
    if deg_50C < 1:
        interpretation["50°C"] = (
            "🟢 Thermally Stable",
            "RNA remains stable at elevated temperature."
        )
    elif deg_50C < 2:
        interpretation["50°C"] = (
            "🟡 Moderate Thermal Stability",
            "Some degradation occurs due to heat."
        )
    else:
        interpretation["50°C"] = (
            "🔴 Thermally Unstable",
            "Heat significantly degrades the RNA."
        )

    # Mg + 50°C
    if deg_Mg_50C < 1:
        interpretation["Mg + 50°C"] = (
            "🟢 Stable",
            "Magnesium improves thermal stability."
        )
    elif deg_Mg_50C < 2:
        interpretation["Mg + 50°C"] = (
            "🟡 Moderate Stability",
            "Magnesium offers limited protection."
        )
    else:
        interpretation["Mg + 50°C"] = (
            "🔴 Unstable",
            "RNA still degrades considerably despite magnesium."
        )

    return interpretation