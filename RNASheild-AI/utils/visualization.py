# ==========================================
# visualization.py
# ==========================================

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


# ==========================================
# Line Chart
# ==========================================

def plot_degradation(prediction):

    """
    prediction shape = (68,5)

    Column 0 -> Reactivity
    Column 1 -> deg_pH10
    Column 2 -> deg_Mg_pH10
    Column 3 -> deg_50C
    Column 4 -> deg_Mg_50C
    """

    positions = list(range(1, 69))

    fig = go.Figure()

    names = [
        "Reactivity",
        "deg_pH10",
        "deg_Mg_pH10",
        "deg_50C",
        "deg_Mg_50C"
    ]

    for i in range(5):

        fig.add_trace(

            go.Scatter(

                x=positions,

                y=prediction[:, i],

                mode="lines+markers",

                name=names[i]

            )

        )

    fig.update_layout(

        title="RNA Stability Across Nucleotide Positions",

        xaxis_title="Nucleotide Position",

        yaxis_title="Predicted Value",

        template="plotly_white",

        hovermode="x unified",

        height=550

    )

    return fig


# ==========================================
# Heatmap
# ==========================================

def plot_heatmap(prediction):

    labels = [

        "Reactivity",

        "deg_pH10",

        "deg_Mg_pH10",

        "deg_50C",

        "deg_Mg_50C"

    ]

    df = pd.DataFrame(

        prediction.T,

        index=labels,

        columns=list(range(1,69))

    )

    fig = px.imshow(

        df,

        labels=dict(

            x="Nucleotide Position",

            y="Prediction",

            color="Value"

        ),

        aspect="auto",

        title="RNA Degradation Heatmap"

    )

    fig.update_layout(

        height=350

    )

    return fig


# ==========================================
# Average Prediction Bar Chart
# ==========================================

def plot_average_scores(avg_prediction):

    labels = [

        "Reactivity",

        "deg_pH10",

        "deg_Mg_pH10",

        "deg_50C",

        "deg_Mg_50C"

    ]

    fig = px.bar(

        x=labels,

        y=avg_prediction,

        text=avg_prediction.round(2),

        title="Average Prediction Scores"

    )

    fig.update_layout(

        yaxis_title="Average Value",

        xaxis_title="Prediction",

        height=450

    )

    return fig


# ==========================================
# Stability Gauge
# ==========================================

def plot_health_score(score):

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=score,

            title={"text":"RNA Health Score"},

            gauge={

                "axis":{"range":[0,100]},

                "bar":{"color":"green"},

                "steps":[

                    {"range":[0,40],"color":"red"},

                    {"range":[40,70],"color":"yellow"},

                    {"range":[70,100],"color":"lightgreen"}

                ]

            }

        )

    )

    fig.update_layout(

        height=350

    )

    return fig