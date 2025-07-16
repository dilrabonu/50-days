import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
from core.predictor import classifier, _build_feature_vector

STATIC_FEATURES = ['duration_sec', 'publish_hour', 'publish_day']

def show_feature_importance(title, duration, hour, day):
    X = _build_feature_vector(title, duration, hour, day)
    # Get feature importances from the classifier
    importances = classifier.feature_importances_

    feature_labels = STATIC_FEATURES + [f'title_emb_{i}' for i in range(X.shape[1] - len(STATIC_FEATURES))]
    importance_series = pd.Series(importances, index=feature_labels)

    top_static = importance_series[STATIC_FEATURES]
    top_embed = importance_series.drop(STATIC_FEATURES).nlargest(5)
  
    fig, ax = plt.subplots(figsize=(10, 6))
    top_combined = pd.concat([top_static, top_embed])
    sns.barplot(x=top_combined.values, y=top_combined.index, ax=ax )
    plt.set_title('Top Contributing Features')
    plt.set_xlabel('Feature Importance')
    plt.ylabel('Features')
    
    st.pyplot(fig)

    st.caption('Static = Duration, Hour, Day. BERT = Most impactful title word components.')
    
    