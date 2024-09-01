import streamlit as st

# Set page configuration
st.set_page_config(page_title="Student Kit 2024", layout="wide")

# Define the list of applications
apps = {
    "Educational Resource Recommender System": "https://ersystem.streamlit.app/",
    "Fun Facts Generator": "https://fffstduent.streamlit.app/",
    "Screenshot Master": "https://ssmaster.streamlit.app/",
    "LinkedIn Text Formatter": "https://linkedin-text-formatter.streamlit.app/"
}

# Create a top navigation bar
st.markdown("""
    <style>
    .navbar {
        display: flex;
        justify-content: center;
        background-color: #f8f9fa;
        padding: 10px;
        border-bottom: 1px solid #dee2e6;
    }
    .navbar a {
        text-decoration: none;
        color: #007bff;
        margin: 0 15px;
        font-weight: bold;
    }
    .navbar a:hover {
        color: #0056b3;
    }
    </style>
    <div class="navbar">
        <a href="#ersystem">Educational Resource Recommender System</a>
        <a href="#funfacts">Fun Facts Generator</a>
        <a href="#screenshot">Screenshot Master</a>
        <a href="#linkedin">LinkedIn Text Formatter</a>
    </div>
    """, unsafe_allow_html=True)

# Define the app selector
selected_app = st.selectbox("Select an Application", options=list(apps.keys()))

# Display the selected application
app_url = apps[selected_app]

st.markdown(f"""
    <div style="text-align:center;">
        <h2>{selected_app}</h2>
        <iframe src="{app_url}" width="100%" height="800" frameborder="0"></iframe>
    </div>
    """, unsafe_allow_html=True)
