import streamlit as st

# Set page configuration
st.set_page_config(page_title="Student Kit 2024", layout="wide")

# Define applications and their URLs
apps = {
    "Educational Resource Recommender System": "https://ersystem.streamlit.app/",
    "Fun Facts Generator": "https://fffstduent.streamlit.app/",
    "Screenshot Master": "https://ssmaster.streamlit.app/",
    "LinkedIn Text Formatter": "https://linkedin-text-formatter.streamlit.app/"
}

# Get the selected application from query parameters
selected_app = st.experimental_get_query_params().get("app", [list(apps.keys())[0]])[0]

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
    }
    .header {
        background-color: #1E1E1E;
        color: white;
        padding: 1rem;
        text-align: center;
    }
    .nav {
        background-color: #333;
        display: flex;
        justify-content: center;
        padding: 0.5rem;
        position: fixed;
        top: 0;
        width: 100%;
        z-index: 1000;
    }
    .nav a {
        color: white;
        padding: 0.5rem 1rem;
        text-decoration: none;
        font-size: 18px;
        font-weight: bold;
        display: inline-block;
    }
    .nav a:hover {
        background-color: #575757;
    }
    .nav a.active {
        background-color: #575757;
    }
    .content {
        margin-top: 60px; /* Adjust for navbar height */
        padding: 1rem;
        text-align: center;
    }
    iframe {
        border: none;
        width: 100%;
        height: 800px; /* Adjust as needed */
    }
    .footer {
        background-color: #1E1E1E;
        color: white;
        text-align: center;
        padding: 1rem;
        position: fixed;
        bottom: 0;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Create the header
st.markdown('<div class="header"><h1>🎓 Student Kit 2024</h1></div>', unsafe_allow_html=True)

# Create the navigation bar with links to each app
nav_links = "".join([
    f'<a href="?app={app_name}" class={"active" if app_name == selected_app else ""}>{app_name}</a>'
    for app_name in apps.keys()
])

st.markdown(f'''
    <div class="nav">
        {nav_links}
    </div>
''', unsafe_allow_html=True)

# Content Area
st.markdown('<div class="content">', unsafe_allow_html=True)
st.markdown(f'<h2>{selected_app}</h2>', unsafe_allow_html=True)
st.markdown(f'<iframe src="{apps[selected_app]}"></iframe>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer"><p>© 2024 Student Kit 2024 | All rights reserved</p></div>', unsafe_allow_html=True)
