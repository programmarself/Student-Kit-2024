import streamlit as st

# Set page configuration
st.set_page_config(page_title="Student Kit 2024", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        font-family: Arial, sans-serif;
    }
    .main {
        padding: 2rem;
    }
    .header {
        background-color: #1E1E1E;
        color: white;
        padding: 1rem;
        text-align: center;
    }
    .nav {
        background-color: #333;
        overflow: hidden;
    }
    .nav a {
        float: left;
        display: block;
        color: white;
        text-align: center;
        padding: 14px 16px;
        text-decoration: none;
    }
    .nav a:hover {
        background-color: #ddd;
        color: black;
    }
    .content {
        margin: 1rem;
    }
    iframe {
        border: none;
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

# Header
st.markdown('<div class="header"><h1>🎓 Student Kit 2024</h1></div>', unsafe_allow_html=True)

# Navigation Bar
st.markdown("""
    <div class="nav">
        <a href="#app1">Educational Resource Recommender System</a>
        <a href="#app2">Fun Facts Generator</a>
        <a href="#app3">Screenshot Master</a>
        <a href="#app4">LinkedIn Text Formatter</a>
    </div>
    """, unsafe_allow_html=True)

# Main Content Area
st.markdown('<div class="main">', unsafe_allow_html=True)

# Application 1
st.markdown('<div id="app1" class="content"><h2>Educational Resource Recommender System</h2>', unsafe_allow_html=True)
st.markdown('<iframe src="https://ersystem.streamlit.app/" width="100%" height="600"></iframe>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Application 2
st.markdown('<div id="app2" class="content"><h2>Fun Facts Generator</h2>', unsafe_allow_html=True)
st.markdown('<iframe src="https://fffstduent.streamlit.app/" width="100%" height="600"></iframe>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Application 3
st.markdown('<div id="app3" class="content"><h2>Screenshot Master</h2>', unsafe_allow_html=True)
st.markdown('<iframe src="https://ssmaster.streamlit.app/" width="100%" height="600"></iframe>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Application 4
st.markdown('<div id="app4" class="content"><h2>LinkedIn Text Formatter</h2>', unsafe_allow_html=True)
st.markdown('<iframe src="https://linkedin-text-formatter.streamlit.app/" width="100%" height="600"></iframe>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer"><p>© 2024 Student Kit 2024 | All rights reserved</p></div>', unsafe_allow_html=True)
