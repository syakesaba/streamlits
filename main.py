import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App")

st.write("Hello, Streamlit! This is a simple example.")

# Create some sample data
data = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['Column A', 'Column B']
)

st.line_chart(data)
