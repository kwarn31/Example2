# Example 2
# NOTE: must name ".py" or streamlit will not recognize the file
import streamlit as st
import plotly.express as px
import pandas as pd

# Load Sample Data
df = px.data.gapminder()

# Title of the app
st.title("Interactive Dashboard with Streamlit and Plotly")

# Select Year with Slider
year = st.slider("Select Year:", int(df["year"].min()), int(df["year"].max()), int(df["year"].min()))

# Filter Data
filtered_df = df[df["year"] == year]

# Create Plotly Scatter Plot
fig = px.scatter(filtered_df, x = "gdpPercap", y = "lifeExp", size = "pop", color = "continent", hover_name = "country", log_x = True, size_max = 60)

# Display Plotly Chart
st.plotly_chart(fig)

# COPY and PASTE all of the above from this cell into the github repository
