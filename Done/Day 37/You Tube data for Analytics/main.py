# app/main.py
import sys
import os
import streamlit as st

# Add project root to sys.path so 'app', 'core', etc. can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.ui import show_ui

def main():
    st.set_page_config(page_title="TitleBoost.AI", layout="centered")
    st.title("🚀 TitleBoost.AI – YouTube Title Performance Predictor & Coach")
    st.markdown("""
        Maximize your YouTube video's impact. Enter a title and get:
        - 📈 Predicted views
        - 🔥 Virality class (Low / Medium / High)
        - 💡 AI-powered title suggestions
        - 📊 Explanation of why your title may succeed (or not)
    """)
    show_ui()

if __name__ == '__main__':
    main()
