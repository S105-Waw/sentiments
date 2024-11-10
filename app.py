import pandas as pd
import streamlit as st
from datetime import datetime

# Load the CSV data (replace with actual path if needed)
df = pd.read_csv('knowledge_data.csv')

# Initialize Streamlit page layout with sidebar open by default and reduced sidebar size
st.set_page_config(page_title="Cloud-Based Knowledge Management", page_icon=":bar_chart:", layout="wide", initial_sidebar_state="expanded")

# Custom CSS to adjust sidebar size
st.markdown("""
    <style>
        /* Make the sidebar smaller */
        .css-1d391kg {
            width: 220px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar elements (Open by default)
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

# Knowledge Addition Section
st.subheader("➕ Add New Knowledge Entry")

with st.form("add_knowledge_form"):
    # Create input fields for new knowledge entry
    title = st.text_input("Title")
    content_type = st.selectbox("Content Type", ["Article", "Document", "Research Paper", "Tutorial", "Other"])
    author = st.text_input("Author")
    date_created = st.date_input("Date Created", datetime.today())
    last_updated = st.date_input("Last Updated", datetime.today())
    access_frequency = st.slider("Access Frequency", 1, 100, 1)
    
    # Submit button to add the new knowledge entry
    submit_button = st.form_submit_button("Add Knowledge")
    
    if submit_button:
        # Validation: Check if any of the fields are empty
        if not title or not author or not content_type:
            st.error("❗ All fields must be filled out! Please make sure all fields are completed before submitting.")
        else:
            # Create a new row of data
            new_data = {
                "Title": title,
                "Content_Type": content_type,
                "Author": author,
                "Date_Created": str(date_created),
                "Last_Updated": str(last_updated),
                "Access_Frequency": access_frequency
            }
            
            # Append the new data to the DataFrame
            df = df.append(new_data, ignore_index=True)
            
            # Save the updated DataFrame back to the CSV file
            df.to_csv('knowledge_data.csv', index=False)
            
            # Show a confirmation message
            st.success("New knowledge entry added successfully!")
            st.write(f"Title: {title}")
            st.write(f"Content Type: {content_type}")
            st.write(f"Author: {author}")
            st.write(f"Date Created: {date_created}")
            st.write(f"Last Updated: {last_updated}")
            st.write(f"Access Frequency: {access_frequency}")

# Footer section
st.markdown("""
    ---
    Made with ❤️ by [Your Name]
""")
