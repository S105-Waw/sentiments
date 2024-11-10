# Import necessary libraries
import pandas as pd
import streamlit as st
from datetime import datetime

# Load the CSV data (replace with actual path if needed)
df = pd.read_csv('knowledge_data.csv')

# Initialize Streamlit page layout
st.set_page_config(page_title="Cloud-Based Knowledge Management", page_icon=":bar_chart:", layout="wide")

# Sidebar elements
with st.sidebar:
    # Display the date of the day
    st.markdown(f"### 📅 Date: {datetime.now().strftime('%Y-%m-%d')}")

    # Display a welcome message
    st.markdown("### 👋 Welcome to the Knowledge Management Dashboard")
    st.markdown("This dashboard helps you explore and manage organizational knowledge effectively.")

    # About Section
    st.markdown("### ℹ️ About")
    st.markdown("""
    This app is designed to manage knowledge within an organization. 
    You can search for articles, documents, and resources based on various categories and access frequency. 
    The system provides insights into knowledge distribution and trends, improving data-driven decision-making.
    """)

    # Optional: Add a small image or logo in the sidebar (you can add your image URL here)
    # st.image("https://via.placeholder.com/150", width=150)

# Main page content
st.title("🌟 Cloud-Based Knowledge Management Dashboard")

# Display the column names to check for any discrepancies
st.subheader("Column Names in the Dataset")
st.write(df.columns)

# Display a sample of the knowledge data
st.subheader("Sample Knowledge Data")
st.dataframe(df.head(10))

# Display the distribution of content types (e.g., articles, documents)
if 'Content_Type' in df.columns:
    st.subheader("📊 Knowledge Distribution by Content Type")
    content_type_counts = df['Content_Type'].value_counts()
    st.bar_chart(content_type_counts)
else:
    st.warning("The 'Content_Type' column is not found in the dataset.")

# Display the frequency of access for each knowledge entry
if 'Access_Frequency' in df.columns:
    st.subheader("📉 Knowledge Access Frequency")
    access_frequency_counts = df['Access_Frequency'].value_counts()
    st.bar_chart(access_frequency_counts)
else:
    st.warning("The 'Access_Frequency' column is not found in the dataset.")

# Initialize search_results to be an empty dataframe
search_results = pd.DataFrame()

# Search Knowledge Section
st.subheader("🔍 Search Knowledge")
search_term = st.text_input("Enter a keyword to search in the Title or Content Type:")
if search_term:
    search_results = df[df['Title'].str.contains(search_term, case=False, na=False) | df['Content_Type'].str.contains(search_term, case=False, na=False)]
    st.write("### 🧠 Search Results:")
    st.dataframe(search_results)

# Optionally, allow downloading the filtered search results
if not search_results.empty:
    st.download_button(
        label="📥 Download Search Results",
        data=search_results.to_csv(index=False),
        file_name="filtered_knowledge_data.csv",
        mime="text/csv"
    )

# Footer section
st.markdown("""
    ---
    Made with ❤️ by [Your Name]
""")
