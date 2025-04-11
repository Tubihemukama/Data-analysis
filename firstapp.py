import streamlit as st
import pandas as pd

st.title("Excel Variable Analyzer 📊")

upload = st.file_uploader('Upload an Excel File', type=['xlsx'])

if upload is not None:
    dataset = pd.read_excel(upload)
    st.subheader("Preview of Uploaded Dataset")
    st.write(dataset.head())

    non_numeric_variable_list = dataset.select_dtypes(include=['object', 'string', 'category']).columns

    def non_numeric_variables():
        all_tables = []
        for var in non_numeric_variable_list:
            frequency_table = dataset[var].value_counts().reset_index()
            frequency_table.columns = ['Category', 'Frequency']
            frequency_table['Percentage'] = (frequency_table['Frequency'] / frequency_table['Frequency'].sum()) * 100
            frequency_table['Variable'] = var
            frequency_table = frequency_table[['Variable', 'Category', 'Frequency', 'Percentage']]
            all_tables.append(frequency_table)

        combined_table = pd.concat(all_tables, ignore_index=True)
        st.subheader("Categorical Variable Summary")
        st.dataframe(combined_table)

    non_numeric_variables()
else:
    st.warning('📁 Please upload a dataset to proceed.')
