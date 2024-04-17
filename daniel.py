import streamlit as st

def process_uploaded_file(uploaded_file):
    # Your file processing logic goes here
    # For example, if it's a CSV:
    import pandas as pd    
    df = pd.read_csv(uploaded_file)
    st.write(df)  # Display the content

st.title("File Uploader App")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    process_uploaded_file(uploaded_file)