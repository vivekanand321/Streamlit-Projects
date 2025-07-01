import numpy as np
import pandas as pd
import streamlit as st

st.title("🎉 Your UV Setup is Working!")

# Create some sample data using pandas and numpy
st.header("Sample Data Analysis")

# Use numpy and pandas to demonstrate the imports
data = {"x": np.random.randn(100), "y": np.random.randn(100)}
df = pd.DataFrame(data)

st.write("Here's some sample data:")
st.dataframe(df.head())

st.write("Basic statistics:")
st.write(df.describe())
