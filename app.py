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
def get_nav_links():
    return "".join([
        f'<a href="/?app={app_name}" class="nav-link">{app_name}</a>'
        for app_name in apps.keys()
    ])

# Get the selected application from query parameters
def get_selected_app():
    query_params = st.experimental_get_query_params()
    return query_params.get("app", [list(apps.keys())[0]])[0]

# Set up the navigation bar and content layout
def display_page():
    selected_app = get_selected_app()

    # Create the navigation bar
    st.markdown(f"""
    <style>
        body {{
            margin: 0;
            font-family: Arial, sans-serif;
        }}
        .navbar {{
            display: flex;
            justify-content: center;
            background-color: #1E1E1E;
            padding: 10px 0;
            position: fixed;
            top: 0;
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
            border-radius: 5px;
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
            margin-top: 60px; /* Adjust for navbar height */
            padding: 20px;
            text-align: center;
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
        .footer {{
            background-color: #1E1E1E;
            color: white;
            text-align: center;
            padding: 1rem;
            position: fixed;
            bottom: 0;
            width: 100%;
        }}
    </style>
    <div class="navbar">
        {get_nav_links()}
    </div>
    <div class="content">
        <div class="app-header">{selected_app}</div>
        <iframe class="app-frame" src="{apps[selected_app]}"></iframe>
    </div>
    <div class="footer">
        <p>© 2024 Student Kit 2024 | All rights reserved</p>
    </div>
    """, unsafe_allow_html=True)

# Display the page content
display_page()
