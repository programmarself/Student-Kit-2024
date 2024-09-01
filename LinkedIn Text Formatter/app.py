import streamlit as st
import streamlit.components.v1 as components

# Function to apply unicode formatting
def apply_unicode_formatting(text, bold, italic, underline, strikethrough):
    if bold:
        text = ''.join([chr(ord('𝐀') + (ord(c) - ord('A'))) if 'A' <= c <= 'Z' else chr(ord('𝐚') + (ord(c) - ord('a'))) if 'a' <= c <= 'z' else c for c in text])
    if italic:
        text = ''.join([chr(ord('𝑨') + (ord(c) - ord('A'))) if 'A' <= c <= 'Z' else chr(ord('𝒂') + (ord(c) - ord('a'))) if 'a' <= c <= 'z' else c for c in text])
    if strikethrough:
        text = ''.join([c + '\u0336' for c in text])
    return text

# Streamlit app layout
st.title("LinkedIn Text Formatter")
ext = st.text("Developed By: Irfan Ullah Khan")

text = st.text_area("Enter your text here:", height=150)

# Checkbox options for formatting
bold = st.checkbox("Bold")
italic = st.checkbox("Italic")
strikethrough = st.checkbox("Strikethrough")

# Apply formatting
formatted_text = apply_unicode_formatting(text, bold, italic, underline=False, strikethrough=strikethrough)

# Display formatted text
st.text_area("Formatted text (copy this):", formatted_text, height=150)

# JavaScript code to copy text
copy_js = """
<script>
function copyText() {
    var copyText = document.getElementById("formatted-text");
    navigator.clipboard.writeText(copyText.innerText).then(function() {
        // Optionally: alert("Text copied to clipboard!");
    }, function(err) {
        // Optionally: alert("Failed to copy text: " + err);
    });
}
document.getElementById("copy-button").addEventListener("click", copyText);
</script>
"""

# Display copy button and JavaScript
components.html(f"""
    <button id="copy-button">Copy Text</button>
    <div id="formatted-text" style="display: none;">{formatted_text}</div>
    {copy_js}
""", height=100)
