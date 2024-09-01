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
    "App 1: Educational Resource Recommender System": "https://ersystem.streamlit.app/",
    "App 2: Fun Facts Generator": "https://fffstduent.streamlit.app/",
    "App 3: Screenshot Master": "https://ssmaster.streamlit.app/",
    "App 4: LinkedIn Text Formatter": "https://linkedin-text-formatter.streamlit.app/"
}

# Display each app in an iframe
for name, url in apps.items():
    st.header(name)
    st.markdown(f'<iframe src="{url}" width="100%" height="600" frameborder="0"></iframe>', unsafe_allow_html=True)
