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

# Display the distribution of content types (e.g., articles, documents)
if 'Content_Type' in df.columns:
    st.subheader("Knowledge Distribution by Content Type")
    content_type_counts = df['Content_Type'].value_counts()
    st.bar_chart(content_type_counts)
else:
    st.warning("The 'Content_Type' column is not found in the dataset.")

# Display the frequency of access for each knowledge entry
if 'Access_Frequency' in df.columns:
    st.subheader("Knowledge Access Frequency")
    access_frequency_counts = df['Access_Frequency'].value_counts()
    st.bar_chart(access_frequency_counts)
else:
    st.warning("The 'Access_Frequency' column is not found in the dataset.")

# Allow the user to search for knowledge entries based on the 'Title' or 'Content_Type'
st.subheader("Search Knowledge")
search_term = st.text_input("Enter a keyword to search in the Title or Content Type:")
if search_term:
    search_results = df[df['Title'].str.contains(search_term, case=False, na=False) | df['Content_Type'].str.contains(search_term, case=False, na=False)]
    st.write("Search Results:")
    st.dataframe(search_results)

# Optionally, allow downloading the filtered search results
if not search_results.empty:
    st.download_button(
        label="Download Search Results",
        data=search_results.to_csv(index=False),
        file_name="filtered_knowledge_data.csv",
        mime="text/csv"
    )
