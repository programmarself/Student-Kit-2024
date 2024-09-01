import streamlit as st

# Set page configuration
st.set_page_config(page_title="Student Kit 2024", layout="wide")

# Title and description with custom styling
st.markdown("""
    <style>
    .title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
    }
    .description {
        font-size: 18px;
        text-align: center;
        margin-bottom: 20px;
    }
    .app-container {
        margin-bottom: 40px;
    }
    </style>
    <p class="title">🎓 Student Kit 2024</p>
    <p class="description">
        Welcome to Student Kit 2024, your all-in-one platform for educational tools and resources.
        Explore and use the following applications:
    </p>
""", unsafe_allow_html=True)

# List of applications with their names and URLs
apps = {
    "Educational Resource Recommender System": "https://ersystem.streamlit.app/",
    "Fun Facts Generator": "https://fffstduent.streamlit.app/",
    "Screenshot Master": "https://ssmaster.streamlit.app/",
    "LinkedIn Text Formatter": "https://linkedin-text-formatter.streamlit.app/"
}

# Display each app in a styled iframe
for name, url in apps.items():
    st.markdown(f"""
        <div class="app-container">
            <h2>{name}</h2>
            <iframe src="{url}" width="100%" height="700" frameborder="0"></iframe>
        </div>
    """, unsafe_allow_html=True)
