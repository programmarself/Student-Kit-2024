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
        text-align: center;
    }
    .nav a {
        color: white;
        text-decoration: none;
        margin: 0 1rem;
        font-weight: bold;
    }
    .nav a:hover {
        text-decoration: underline;
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

# Sidebar for application selection
app_option = st.sidebar.selectbox(
    "Choose an application:",
    ["Educational Resource Recommender System", 
     "Fun Facts Generator", 
     "Screenshot Master", 
     "LinkedIn Text Formatter"]
)

# Main content area
st.markdown('<div class="content">', unsafe_allow_html=True)

# Display the selected application
if app_option == "Educational Resource Recommender System":
    st.header("Educational Resource Recommender System")
    st.markdown('<iframe src="https://ersystem.streamlit.app/" width="100%" height="600"></iframe>', unsafe_allow_html=True)
elif app_option == "Fun Facts Generator":
    st.header("Fun Facts Generator")
    st.markdown('<iframe src="https://fffstduent.streamlit.app/" width="100%" height="600"></iframe>', unsafe_allow_html=True)
elif app_option == "Screenshot Master":
    st.header("Screenshot Master")
    st.markdown('<iframe src="https://ssmaster.streamlit.app/" width="100%" height="600"></iframe>', unsafe_allow_html=True)
elif app_option == "LinkedIn Text Formatter":
    st.header("LinkedIn Text Formatter")
    st.markdown('<iframe src="https://linkedin-text-formatter.streamlit.app/" width="100%" height="600"></iframe>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer"><p>© 2024 Student Kit 2024 | All rights reserved</p></div>', unsafe_allow_html=True)
