import streamlit as st
import joblib
import pandas as pd

# Load model and preprocessor
model = joblib.load('burnout_model.pkl')
preprocessor = joblib.load('preprocessor.pkl')
label_map = joblib.load('label_map.pkl')

# Upload new employee data
uploaded_file = st.file_uploader("Upload employee CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Preprocess
    X_transformed = preprocessor.transform(df)

    # Predict
    predictions = model.predict(X_transformed)
    df["Predicted Burnout Level"] = predictions

    # Convert numeric prediction to label
    df["Predicted Burnout Label"] = df["Predicted Burnout Level"].map(label_map)

    # Display results
    st.write(df)
