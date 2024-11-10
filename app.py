# Import necessary libraries
import pandas as pd
import streamlit as st

# Load the CSV data
df = pd.read_csv('knowledge_data.csv')

# Initialize Streamlit
st.title("Cloud-Based Knowledge Management Dashboard")

# Display a sample of the knowledge data
st.subheader("Sample Knowledge Data")
st.dataframe(df.head(10))

# Knowledge Distribution by Category
st.subheader("Knowledge Distribution by Category")
category_counts = df['Category'].value_counts()
st.bar_chart(category_counts)

# Knowledge Entries by Department
st.subheader("Knowledge Entries by Department")
department_counts = df['Department'].value_counts()
st.bar_chart(department_counts)

# Allow the user to search for knowledge entries
st.subheader("Search Knowledge")
search_term = st.text_input("Enter a keyword to search:")
if search_term:
    search_results = df[df['Content'].str.contains(search_term, case=False)]
    st.write("Search Results:")
    st.dataframe(search_results)
