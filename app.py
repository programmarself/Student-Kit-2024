import streamlit as st

# Set page configuration
st.set_page_config(page_title="Student Kit 2024", layout="wide")

# Title and description
st.title("🎓 Student Kit 2024")
st.markdown("""
    Welcome to Student Kit 2024, your all-in-one platform for educational tools and resources.
    Explore and use the following applications:
""")

# List of applications with their names and URLs
apps = {
    "App 1: Educational Resource Finder": "https://your-app1-url.streamlit.app",
    "App 2: Fun Facts Generator": "https://your-app2-url.streamlit.app",
    "App 3: Interactive Learning Tools": "https://your-app3-url.streamlit.app",
    "App 4: Text Formatter": "https://your-app4-url.streamlit.app"
}

# Display each app in an iframe
for name, url in apps.items():
    st.header(name)
    st.markdown(f'<iframe src="{url}" width="100%" height="600" frameborder="0"></iframe>', unsafe_allow_html=True)
