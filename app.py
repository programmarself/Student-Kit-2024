import streamlit as st
from streamlit.components.v1 import html

# Set page configuration
st.set_page_config(page_title="Student Kit 2024", layout="wide")

# Define the list of applications
apps = {
    "Educational Resource Recommender System": "https://ersystem.streamlit.app/",
    "Fun Facts Generator": "https://fffstduent.streamlit.app/",
    "Screenshot Master": "https://ssmaster.streamlit.app/",
    "LinkedIn Text Formatter": "https://linkedin-text-formatter.streamlit.app/"
}

# Create a top navigation bar with clickable links
nav_links = "".join([f'<a href="javascript:void(0);" onclick="document.getElementById(\'app-frame\').src=\'{url}\';">{name}</a>' 
                     for name, url in apps.items()])

nav_html = f"""
    <style>
    .navbar {{
        display: flex;
        justify-content: center;
        background-color: #f8f9fa;
        padding: 10px;
        border-bottom: 1px solid #dee2e6;
    }}
    .navbar a {{
        text-decoration: none;
        color: #007bff;
        margin: 0 15px;
        font-weight: bold;
    }}
    .navbar a:hover {{
        color: #0056b3;
    }}
    </style>
    <div class="navbar">
        {nav_links}
    </div>
    <div style="text-align:center;">
        <iframe id="app-frame" src="{list(apps.values())[0]}" width="100%" height="800" frameborder="0"></iframe>
    </div>
    """

# Display the HTML in Streamlit
html(nav_html, height=900, scrolling=True)
