Interactive Sentiment Analysis Dashboard

This project is an Interactive Sentiment Analysis Dashboard built with Streamlit and powered by a pre-trained sentiment analysis model from the Hugging Face Transformers library.
The app allows you to upload a CSV file containing text data  and performs sentiment analysis on the uploaded data.

Features
CSV File Upload: Easily upload a CSV file for sentiment analysis.
Data Preview: View a sample of your uploaded data to ensure it is loaded correctly.
Sentiment Analysis: Analyze the sentiment of text data using a pre-trained natural language processing (NLP) model.
Results Display: See the sentiment (positive, negative, or neutral) and the confidence score for each text entry.
Interactive Charts: Visualize the distribution of sentiments in your dataset using bar charts.
How to Run the App
Install Dependencies: Make sure you have Python installed on your system. You also need to install the required libraries:

pip install streamlit pandas transformers
Run the Streamlit App: Use the following command in your terminal to launch the app:

streamlit run app.py
Upload a CSV File:

The app expects a CSV file with a column named Review. This column should contain the text data you want to analyze.
Use the file uploader on the sidebar to upload your CSV file.
View Results:

Once the file is uploaded, the app will display a sample of your data, perform sentiment analysis, and show the analyzed results.
You can also view the distribution of sentiments in a bar chart.

Project Structure


├── app.py   

├── README.md 


└── requirements.txt    

Requirements
Python: Version 3.7 or higher
Libraries:
streamlit: For building the web app
pandas: For data manipulation
transformers: For NLP model and sentiment analysis
You can install all dependencies using the requirements.txt file:

pip install -r requirements.txt

Usage Guide

Data Upload: Use the sidebar to upload your CSV file. Ensure your file has a Review column.
Data Preview: The app will display the first few rows of your data and the column names for verification.

Sentiment Analysis: The sentiment analysis results, including the sentiment label and confidence score, will be shown alongside your data.
Visualization: A bar chart will illustrate the distribution of sentiments in your dataset.

Model Information

The app uses a pre-trained sentiment analysis model from the Hugging Face Transformers library. By default, 
it uses DistilBERT for sentiment analysis, which is fine-tuned on the SST-2 dataset for binary sentiment classification.

Note: Using the default model in a production environment without specifying a model name and revision is not recommended.
 You can customize the model for better performance or specific use cases.

Example CSV File

Your CSV file should have a structure similar to this:

Review
"I love this product! It works great."
"Terrible experience, would not buy."
"It's okay, nothing special."

About

This app was created to make sentiment analysis easy and accessible for non-technical users. It is ideal for 
quickly analyzing customer reviews or any other textual feedback data.

Future Enhancements

Custom Model Selection: Allow users to choose from different pre-trained models.
Text Cleaning Options: Add preprocessing features like text cleaning and tokenization.
Sentiment Export: Provide an option to download the analyzed data as a CSV file.

Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request with your changes.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
If you have any questions or need further assistance, feel free to reach out to me.
