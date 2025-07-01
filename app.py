import numpy as np
import pandas as pd
import streamlit as st

# Set page title
st.title("🎉 Your UV Setup is Working!")

# Create some sample data using pandas and numpy
st.header("Sample Data Analysis")

# Generate random data
np.random.seed(42)
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": np.random.randint(20, 60, 5),
    "Score": np.random.randint(60, 100, 5),
}

df = pd.DataFrame(data)

# Display the dataframe
st.subheader("Sample DataFrame:")
st.write(df)

# Show some basic statistics
st.subheader("Basic Statistics:")
st.write(df.describe())

# Create a simple chart
st.subheader("Age vs Score Chart:")
st.scatter_chart(df.set_index("Name")[["Age", "Score"]])

# Show package versions
st.subheader("Package Versions:")
st.write(f"- Pandas: {pd.__version__}")
st.write(f"- NumPy: {np.__version__}")
st.write(f"- Streamlit: {st.__version__}")

st.success("✅ All packages are working correctly!")
