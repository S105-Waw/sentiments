import streamlit as st  # Streamlit for the dashboard and deployment
import pandas as pd
from transformers import pipeline

# Setting up the page layout
st.set_page_config(page_title="Sentiment Analysis Dashboard", page_icon=":bar_chart:", layout="wide")

# Title of the Dashboard
st.title("🌟 Interactive Sentiment Analysis Dashboard")

# Sidebar for file upload and instructions
st.sidebar.header("🔍 Upload Your CSV File")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file (must include 'Review' column)", type=["csv"])

st.sidebar.subheader("💡 Sentiment Analysis Model")

# Using the sentiment-analysis pipeline with TensorFlow backend
classifier = pipeline('sentiment-analysis', framework='tf')

# Displaying instructions or alerts
if uploaded_file is None:
    st.sidebar.info("Upload a CSV to begin sentiment analysis. Ensure it contains a column named 'Review'.")
else:
    st.sidebar.success("Nice! CSV file uploaded successfully!")

# If a file is uploaded, process it
if uploaded_file is not None:
    try:
        # Load the CSV file
        df = pd.read_csv(uploaded_file)
        st.write("### 📊 Sample of Uploaded Data")
        st.table(df.head())  # Display a static table preview of the data

        # Check if 'Review' column exists
        st.write("### Columns in the Uploaded Data")
        st.table(df.columns)  # Show column names for verification

        if 'Review' not in df.columns:
            st.error("The CSV file must contain a 'Review' column. Please upload a valid file.")
        else:
            # Perform sentiment analysis on the 'Review' column
            st.write("### 🧠 Sentiment Analysis Results")
            df['Sentiment'] = df['Review'].apply(lambda x: classifier(x)[0]['label'])
            df['Confidence'] = df['Review'].apply(lambda x: f"{classifier(x)[0]['score']*100:.2f}%")

            # Display the updated DataFrame with Sentiment & Confidence columns
            st.write("#### Analyzed Data:")
            st.table(df.head())  # Show a static table with the analysis results

            # Visualize the sentiment distribution
            st.write("### 📊 Sentiment Distribution")
            sentiment_counts = df['Sentiment'].value_counts()
            st.bar_chart(sentiment_counts)

            # Allow the user to download the analyzed data
            st.download_button(
                label="Download Analyzed Data",
                data=df.to_csv(index=False),
                file_name="analyzed_sentiment_data.csv",
                mime="text/csv"
            )
    except Exception as e:
        st.error(f"Error loading or analyzing the file: {e}")
else:
    st.warning("⚠️ Please upload a CSV file to proceed with sentiment analysis.")

# About section
st.sidebar.markdown("### ℹ️ About")
st.sidebar.info("""
This app analyzes the sentiment of customer reviews using a pre-trained sentiment analysis model.
- **Sentiment**: The model classifies each review as either 'POSITIVE' or 'NEGATIVE'.
- **Confidence**: The probability score for each prediction.
""")
