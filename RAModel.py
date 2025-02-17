
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import plotly.express as px




# Streamlit User Interface for Deployed Model
def main():
    st.title('🏠 BFSI Regulatory Assistant')
    st.write('Help you on Regulatory Compliance')
    
    # Train model
    # model = train_model()
    
    # User input
    

    uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

    if uploaded_file is not None:
        df = extract_data(uploaded_file)
    

if __name__ == '__main__':
    main()
