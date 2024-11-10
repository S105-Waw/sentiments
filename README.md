Cloud-Based Knowledge Retention Management System
Overview
The Cloud-Based Knowledge Retention Management System is designed to store, manage, and analyze organizational knowledge such as documents, research papers, articles, and more. This web application enables users to add knowledge entries, search through them, visualize data, and download the stored knowledge as a CSV file. The system also displays key insights such as knowledge distribution by content type and access frequency.

Built with Streamlit, this dashboard is easy to deploy and use, providing a user-friendly interface with interactive features.

Features
Knowledge Search: Users can search for knowledge entries based on the title or content type.
Knowledge Visualization: Visualize knowledge distribution by content type and access frequency.
Add New Knowledge: Users can add new knowledge entries with fields such as title, content type, author, and access frequency.
CSV Download: Users can download the complete dataset or filtered search results as a CSV file.
Dynamic Sidebar: The sidebar includes useful information like date, time, and a welcome message, making the dashboard more interactive.
Technologies Used
Streamlit: Framework for building interactive web applications.
Pandas: Library for data manipulation and handling CSV files.
Python: Core language for backend logic.
CSV: Used for storing and downloading knowledge data.
Installation
Follow the steps below to set up and run the project locally:

Clone the repository:


git clone https://github.com/your-username/knowledge-management-system.git
cd knowledge-management-system
Create a virtual environment:


python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required dependencies:


pip install -r requirements.txt
Run the application:


streamlit run app.py
Open the application:
After running the above command, the application will be available at http://localhost:8501.

Usage
Sidebar Features:
Date: Displays the current date.
Time: Displays the current time.
Welcome Message: Provides a friendly greeting to the user.
About Section: Provides a description of the application and its use.
Main Features:
Search Knowledge: Enter a search term to filter knowledge entries based on title or content type. The results are displayed in a table format.
Knowledge Visualization: See the distribution of knowledge content types and access frequency displayed as bar charts.
Add Knowledge: Add new entries with fields for title, content type, author, date created, last updated, and access frequency. Submitting will update the CSV file.
Download CSV: You can download the complete dataset or the filtered search results at any time as a CSV file.
Example Data:
When you first run the application, you will see a sample of existing knowledge entries. New entries can be added via the provided form, and the CSV file is updated accordingly.

CSV File Format
The knowledge data is stored in a CSV file with the following columns:

Title: The title of the knowledge entry (e.g., article, research paper).
Content_Type: Type of the content (e.g., Article, Research Paper, Document).
Author: The author of the knowledge entry.
Date_Created: The date when the knowledge entry was created.
Last_Updated: The last date the knowledge entry was updated.
Access_Frequency: The frequency of access (number of views, interactions).
Example:
Adding New Knowledge:
The user can add a new knowledge entry by filling out the form with the following details:

Title: "Introduction to AI"
Content Type: "Article"
Author: "John Doe"
Date Created: "2024-11-10"
Last Updated: "2024-11-10"
Access Frequency: 5
Downloading the CSV:
The user can download the CSV file at any time. The download will contain all the knowledge entries, including newly added entries.

Future Enhancements
Authentication: Add user authentication to allow multiple users with different access levels.
Advanced Search: Implement more advanced search functionality, such as filters by date or access frequency.
Knowledge Insights: Add more advanced analytics, such as trending knowledge based on access frequency or categorization.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Streamlit for creating an easy-to-use framework for building data applications.
Pandas for efficient data manipulation and management.



