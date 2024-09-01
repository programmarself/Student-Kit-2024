import streamlit as st

# Set page configuration
st.set_page_config(page_title="Student Kit 2024", layout="wide")

# Title and description
st.title("🎓 Student Kit 2024")
st.markdown("""
    Welcome to Student Kit 2024, your all-in-one platform for educational tools and resources.
    Use the navigation bar to explore and use the following applications:
""")

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
    selection = st.radio("Go to", list(apps.keys()))

# Display the selected app in the main area
app_url = apps.get(selection)

if app_url:
    st.markdown(f"""
        <iframe src="{app_url}" width="100%" height="800" frameborder="0"></iframe>
    """, unsafe_allow_html=True)
