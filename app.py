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

# Generate navigation links
def get_nav_links(selected_app):
    return "".join([
        f'<a href="/?app={app_name}" class="nav-link { "active" if app_name == selected_app else "" }">{app_name}</a>'
        for app_name in apps.keys()
    ])

# Get the selected application from query parameters
def get_selected_app():
    query_params = st.experimental_get_query_params()
    return query_params.get("app", [list(apps.keys())[0]])[0]

# Set up the navigation bar and content layout
def display_page():
    selected_app = get_selected_app()

    # Create the header, navigation bar, and content layout
    st.markdown(f"""
    <style>
        body {{
            margin: 0;
            font-family: Arial, sans-serif;
        }}
        .header {{
            background-color: #1E1E1E;
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 32px;
            font-weight: bold;
            position: sticky;
            top: 0;
            z-index: 1000;
        }}
        .navbar {{
            display: flex;
            justify-content: center;
            background-color: #333;
            padding: 10px;
            position: sticky;
            top: 60px; /* Adjust based on header height */
            width: 100%;
            z-index: 1000;
        }}
        .nav-link {{
            color: #f2f2f2;
            text-align: center;
            padding: 14px 20px;
            text-decoration: none;
            font-size: 18px;
            font-weight: bold;
        }}
        .nav-link:hover {{
            background-color: #575757;
            color: white;
        }}
        .active {{
            background-color: #575757;
            color: white;
        }}
        .content {{
            padding: 20px;
            text-align: center;
            margin-top: 20px; /* Space for sticky navbar */
        }}
        .app-header {{
            font-size: 24px;
            margin-bottom: 20px;
            font-weight: bold;
        }}
        .app-frame {{
            width: 100%;
            height: 800px;
            border: none;
        }}
    </style>
    <div class="header">
        Student Kit 2024
    </div>
    <div class="navbar">
        {get_nav_links(selected_app)}
    </div>
    <div class="content">
        <div class="app-header">{selected_app}</div>
        <iframe class="app-frame" src="{apps[selected_app]}"></iframe>
    </div>
    """, unsafe_allow_html=True)

# Display the page content
display_page()
# Footer
st.markdown('<div class="footer"><p>© 2024 Student Kit 2024 | All rights reserved</p></div>', unsafe_allow_html=True)