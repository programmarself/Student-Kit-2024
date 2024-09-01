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

# Create the navigation bar
st.markdown("""
    <style>
        .navbar {
            overflow: hidden;
            background-color: #333;
            padding: 10px;
        }
        .navbar a {
            float: left;
            display: block;
            color: #f2f2f2;
            text-align: center;
            padding: 14px 20px;
            text-decoration: none;
            font-size: 18px;
        }
        .navbar a:hover {
            background-color: #ddd;
            color: black;
        }
        .content {
            padding: 20px;
            text-align: center;
        }
        .app-header {
            font-size: 24px;
            margin-top: 20px;
        }
        .app-frame {
            width: 100%;
            height: 800px;
            border: none;
        }
    </style>
    <div class="navbar">
        {nav_links}
    </div>
    <div class="content">
        <div class="app-header">{app_name}</div>
        <iframe class="app-frame" src="{app_url}"></iframe>
    </div>
""", unsafe_allow_html=True)

# Handle navigation and display the selected app
selected_app = st.experimental_get_query_params().get("app", ["Educational Resource Recommender System"])[0]

# Generate navigation links
nav_links = "".join([
    f'<a href="?app={app_name}">{app_name}</a>'
    for app_name in apps.keys()
])

# Display the navigation links and content
st.markdown(f"""
    <script>
        // Set the default application on page load
        const app_name = "{selected_app}";
        document.querySelector(".app-header").innerText = app_name;
        document.querySelector(".app-frame").src = "{apps[selected_app]}";
    </script>
""", unsafe_allow_html=True)

# Function to handle the navigation
def update_app_url(app_name):
    st.experimental_set_query_params(app=app_name)

# Update the selected app if changed
if st.experimental_get_query_params().get("app"):
    selected_app = st.experimental_get_query_params().get("app")[0]

# Render the navigation and selected app
st.markdown(f"""
    <style>
        .navbar a {{
            font-weight: { 'bold' if selected_app == app_name else 'normal' };
        }}
    </style>
""", unsafe_allow_html=True)
