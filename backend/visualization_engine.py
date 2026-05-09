# Generates charts using Plotly
import plotly.express as px


def create_chart(df):

    if df.shape[1] == 2:
        return px.bar(df, x=df.columns[0], y=df.columns[1])

    return None