import streamlit as st

# Set page configuration
st.set_page_config(page_title="Student Kit 2024", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        font-family: Arial, sans-serif;
    }
    .header {
        background-color: #1E1E1E;
        color: white;
        padding: 1rem;
        text-align: center;
    }
    .nav {
        background-color: #333;
        color: white;
        padding: 1rem;
    }
    .nav select {
        background-color: #333;
        color: white;
        border: none;
        padding: 0.5rem;
    }
    .content {
        margin: 1rem;
    }
    iframe {
        border: none;
        width: 100%;
        height: 600px;
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

# Navigation and Content Selector
option = st.selectbox(
    'Select an Application',
    [
        'Select an Application',
        'Educational Resource Recommender System',
        'Fun Facts Generator',
        'Screenshot Master',
        'LinkedIn Text Formatter'
    ]
)

# Content Area
st.markdown('<div class="content">', unsafe_allow_html=True)

if option == 'Educational Resource Recommender System':
    st.markdown('<h2>Educational Resource Recommender System</h2>', unsafe_allow_html=True)
    st.markdown('<iframe src="https://ersystem.streamlit.app/" width="100%" height="600"></iframe>', unsafe_allow_html=True)

elif option == 'Fun Facts Generator':
    st.markdown('<h2>Fun Facts Generator</h2>', unsafe_allow_html=True)
    st.markdown('<iframe src="https://fffstduent.streamlit.app/" width="100%" height="600"></iframe>', unsafe_allow_html=True)

elif option == 'Screenshot Master':
    st.markdown('<h2>Screenshot Master</h2>', unsafe_allow_html=True)
    st.markdown('<iframe src="https://ssmaster.streamlit.app/" width="100%" height="600"></iframe>', unsafe_allow_html=True)

elif option == 'LinkedIn Text Formatter':
    st.markdown('<h2>LinkedIn Text Formatter</h2>', unsafe_allow_html=True)
    st.markdown('<iframe src="https://linkedin-text-formatter.streamlit.app/" width="100%" height="600"></iframe>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer"><p>© 2024 Student Kit 2024 | All rights reserved</p></div>', unsafe_allow_html=True)
