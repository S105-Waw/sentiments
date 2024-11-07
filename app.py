import streamlit as st # I will use this to visualize the dashboard and for deployment
import pandas as pd
from transformers import pipeline, DistilBertTokenizer, DistilBertForSequenceClassification

# Setting up page layout
st.set_page_config(page_title="Sentiment Analysis Dashboard", page_icon=":bar_chart:", layout="wide")

# Title of my Dashboard
st.title("🌟 Interactive Sentiment Analysis Dashboard")

# My Sidebar 
st.sidebar.header("🔍 Upload Your CSV File")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file (must include 'Review' column)", type=["csv"])

st.sidebar.subheader("💡 Sentiment Analysis Model")

# Specifying the model and tokenizer explicitly
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
model = DistilBertForSequenceClassification.from_pretrained(model_name)
tokenizer = DistilBertTokenizer.from_pretrained(model_name)

# Loading the sentiment analysis pipeline with the specific model
classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

# Displaying instructions or alerts
if uploaded_file is None:
    st.sidebar.info("Upload a CSV to begin sentiment analysis. Ensure it contains a column named 'Review'.")
else:
    st.sidebar.success("Nice! CSV file uploaded successfully!")

# When file is uploaded, displaying and analyzing
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.write("### 📊 Sample of Uploaded Data")
        
        st.table(df.head())  # Simpler, static display. Other methods of previewing were not working for me. 




        # Checking columns to be sure 'Review' exists
        st.write("### Columns in the Uploaded Data")
        st.table(df.columns)  # Displaying column names for debugging

        # Making sure the 'Review' column exists
        if 'Review' not in df.columns:
            st.error("The CSV file must contain a 'Review' column. Please upload a valid file.")
        else:
            # Performing sentiment analysis on the 'Review' column
            st.write("### 🧠 Sentiment Analysis Results")
            df['Sentiment'] = df['Review'].apply(lambda x: classifier(x)[0]['label'])
            df['Confidence'] = df['Review'].apply(lambda x: f"{classifier(x)[0]['score']*100:.2f}%")

            # Displaying the updated DataFrame with Sentiment & Confidence columns
            st.write("#### Analyzed Data:")
            st.table(df.head())  # Simpler, static display

            # Visualizing sentiment distribution
            st.write("### 📊 Sentiment Distribution")
            sentiment_counts = df['Sentiment'].value_counts()
            st.bar_chart(sentiment_counts)

            # Allowing user to download the updated file
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
