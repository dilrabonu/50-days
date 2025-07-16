# app/ui.py
import streamlit as st
from core.predictor import predict_view_class, predict_view_count
from core.recommender import get_title_recommendations
from core.explainer import show_feature_importance

def show_ui():
    with st.form(key='title_form'):
        user_title = st.text_input("Enter YouTube Video Title")
        user_duration = st.slider("Video Duration (in seconds)", 30, 3600, 300)
        user_hour = st.slider("Upload Hour (0-23)", 0, 23, 15)
        user_day = st.selectbox("Planned Publish Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        submitted = st.form_submit_button("Predict Performance")

    if submitted:
        with st.spinner("Analyzing title using AI models..."):
            view_count = predict_view_count(user_title, user_duration, user_hour, user_day)
            view_class, proba = predict_view_class(user_title, user_duration, user_hour, user_day)
            recommendations = get_title_recommendations(user_title)

        st.success(f'Predicted View Count: {int(view_count):,}')
        st.markdown(f'### Virality Prediction: **{view_class.upper()}**')
        st.progress(proba[view_class])

        with st.expander("📢 Recommended Improved Titles"):
            for rec in recommendations:
                st.write(f"- {rec}")

        st.markdown("---")
        show_feature_importance(user_title, user_duration, user_hour, user_day)
