import streamlit as st

# Set page configuration
st.set_page_config(page_title="Student Kit 2024", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #003366;
        color: white;
    }
    .sidebar .sidebar-content h1 {
        color: white;
    }
    .iframe-container {
        border: 1px solid #ddd;
        border-radius: 8px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        overflow: hidden;
    }
    .iframe-container iframe {
        width: 100%;
        height: 800px;
        border: none;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #003366;
    }
    .description {
        font-size: 18px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.markdown('<div class="title">🎓 Student Kit 2024</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Welcome to Student Kit 2024, your all-in-one platform for educational tools and resources. Use the navigation bar to explore and use the following applications:</div>', unsafe_allow_html=True)

# Define the application URLs
apps = {
    "Educational Resource Recommender System": "https://ersystem.streamlit.app/",
    "Fun Facts Generator": "https://fffstduent.streamlit.app/",
    "Screenshot Master": "https://ssmaster.streamlit.app/",
    "LinkedIn Text Formatter": "https://linkedin-text-formatter.streamlit.app/"
}

# Sidebar navigation
with st.sidebar:
    st.header("Navigation")
    selection = st.radio("", list(apps.keys()))

# Display the selected app in the main area
app_url = apps.get(selection)

if app_url:
    st.markdown(f"""
        <div class="iframe-container">
            <iframe src="{app_url}"></iframe>
        </div>
    """, unsafe_allow_html=True)
