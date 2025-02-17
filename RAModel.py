
import streamlit as st
import pandas as pd
import numpy as np





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
