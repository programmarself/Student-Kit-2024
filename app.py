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

# Add custom CSS for styling
st.markdown("""
    <style>
        .tabs {
            display: flex;
            justify-content: center;
            background-color: #333;
            padding: 10px;
        }
        .tab {
            color: #f2f2f2;
            text-align: center;
            padding: 14px 20px;
            text-decoration: none;
            font-size: 18px;
            font-weight: bold;
            border: none;
            background: none;
            cursor: pointer;
        }
        .tab:hover {
            background-color: #ddd;
            color: black;
        }
        .tab-content {
            padding: 20px;
            text-align: center;
        }
        .app-frame {
            width: 100%;
            height: 800px;
            border: none;
        }
    </style>
    """, unsafe_allow_html=True)

# Create a tab layout
def display_tabs():
    st.write("<div class='tabs'>", unsafe_allow_html=True)
    for app_name in apps.keys():
        st.write(f"<button class='tab' onclick=\"showTab('{app_name}')\">{app_name}</button>", unsafe_allow_html=True)
    st.write("</div>", unsafe_allow_html=True)
    
    st.write("<div id='tab-content'>", unsafe_allow_html=True)
    for app_name, url in apps.items():
        st.write(f"""
        <div id="{app_name}" class="tab-content" style="display: {'block' if app_name == 'Educational Resource Recommender System' else 'none'}">
            <iframe class="app-frame" src="{url}"></iframe>
        </div>
        """, unsafe_allow_html=True)
    st.write("</div>", unsafe_allow_html=True)
    
    st.write("""
    <script>
        function showTab(appName) {
            var tabs = document.querySelectorAll('.tab-content');
            tabs.forEach(function(tab) {
                tab.style.display = 'none';
            });
            document.getElementById(appName).style.display = 'block';
        }
    </script>
    """, unsafe_allow_html=True)

# Display the tabs and their content
display_tabs()
