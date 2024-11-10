# Import necessary libraries
import pandas as pd
import streamlit as st

# Load the CSV data
df = pd.read_csv('knowledge_data.csv')

# Initialize Streamlit
st.title("Cloud-Based Knowledge Management Dashboard")

# Display the column names to check for any discrepancies
st.subheader("Column Names in the Dataset")
st.write(df.columns)

# Display a sample of the knowledge data
st.subheader("Sample Knowledge Data")
st.dataframe(df.head(10))

# If 'Category' column exists, show the knowledge distribution
if 'Category' in df.columns:
    st.subheader("Knowledge Distribution by Category")
    category_counts = df['Category'].value_counts()
    st.bar_chart(category_counts)
else:
    st.warning("The 'Category' column is not found in the dataset.")

# If 'Department' column exists, show knowledge entries by department
if 'Department' in df.columns:
    st.subheader("Knowledge Entries by Department")
    department_counts = df['Department'].value_counts()
    st.bar_chart(department_counts)
else:
    st.warning("The 'Department' column is not found in the dataset.")

# Allow the user to search for knowledge entries
st.subheader("Search Knowledge")
search_term = st.text_input("Enter a keyword to search:")
if search_term:
    search_results = df[df['Content'].str.contains(search_term, case=False, na=False)]
    st.write("Search Results:")
    st.dataframe(search_results)
