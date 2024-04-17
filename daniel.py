import streamlit as st
import pandas as pd 

def process_uploaded_file(uploaded_file):
    """Creates a DataFrame from the uploaded CSV file."""

    df = pd.read_csv(uploaded_file)
    return df

st.title("CSV to DataFrame")
uploaded_file = st.file_uploader("Choose a CSV file")

if uploaded_file is not None:
    df = process_uploaded_file(uploaded_file)

    # Display the DataFrame
    st.header("Your DataFrame")
    st.dataframe(df) 



    # Display checkboxes for debt assignment
    st.header("Assign Debt")
    for index, row in df.iterrows():
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"Row {index}: {row.to_string()}")  # Display row info
        with col2:
            owner = st.checkbox('Daniel', key=index)
            df.loc[index, 'Debt Owner'] = 'Daniel' if owner else 'Partner'

    # Group by 'Debt Owner' and calculate sums
    st.header("Debt Summary")
    debt_summary = df.groupby('Debt Owner')[df.columns[-2]].sum()  # Assuming the third column contains the values to sum 
    st.write(debt_summary)