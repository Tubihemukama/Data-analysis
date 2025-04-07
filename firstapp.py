import streamlit as st
import pandas as pd
from io import BytesIO

upload = st.file_uploader('Upload an Excel File', type=['xlsx'])

if upload is not None:
    dataset = pd.read_excel(upload)
    st.write(dataset.head())

    



    variable_list = dataset.columns
    numeric_variable_list = dataset.select_dtypes(include='number').columns
    def numeric_varaibles():
        for var in numeric_variable_list:
            mean_var = dataset[var].mean()
            st.write(f"Mean of {var}:{mean_var:.2f}")
    numeric_varaibles()

    non_numeric_variable_list = dataset.select_dtypes(include = ['object', 'string', 'category']).columns
    def non_numeric_vaiables():
        all_tables = []  # list to collect tables
        for var in non_numeric_variable_list:
            frequency_table = dataset[var].value_counts().reset_index()
            frequency_table.columns = ['Category','Frequency']
            frequency_table['Percentage'] = (frequency_table['Frequency']/frequency_table['Frequency'].sum())*100
            frequency_table['Variable'] = var
            frequency_table = frequency_table[['Variable', 'Category', 'Frequency', 'Percentage']]
            all_tables.append(frequency_table) #Tables appended
            
            # Combine all into one DataFrame
        combined_table = pd.concat(all_tables, ignore_index=True)
        st.dataframe(combined_table)
            
    non_numeric_vaiables()

        

else:
    st.warning('Ensure that a dataset is uploaded')

