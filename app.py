import streamlit as st
import pandas as pd
import numpy as np
import joblib
from src.Utility.common import Read_yaml

# Load artifacts
model = joblib.load("artifacts/trainer/model.pkl")
preprocess = joblib.load("artifacts/data_transfomation/preprocess.pkl")
schema = Read_yaml("schema.yaml")
label_map = {0: "Genuine", 1: "Fake"}

st.set_page_config(page_title="Instagram Account Classifier", layout="wide")
st.title("📸 Instagram Account Classification App")
st.markdown("Classify Instagram accounts as **Genuine** or **Fake** based on their profile attributes.")

# --- User Input Mode ---
mode = st.radio("Choose Input Mode:", ("Upload CSV", "Manual Entry"))

if mode == "Upload CSV":
    uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])

    if uploaded_file is not None:
        input_df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully.")

        # Drop target column if exists
        if 'fake' in input_df.columns:
            input_df = input_df.drop(columns=["fake"])

        st.subheader("📄 Uploaded Data")
        st.dataframe(input_df)

        try:
            transformed = preprocess.transform(input_df)
            predictions = model.predict(transformed)
            input_df["Prediction"] = [label_map[int(p)] for p in predictions]
            st.subheader("🔍 Predictions")
            st.dataframe(input_df)
        except Exception as e:
            st.error(f"Prediction failed: {e}")

elif mode == "Manual Entry":
    st.subheader("📝 Enter Feature Values Manually")

    profile_pic = st.selectbox("Has Profile Picture?", [0, 1])
    length_username = st.number_input("Username Length", min_value=1, max_value=100, value=10)
    fullname_words = st.number_input("Number of Words in Full Name", min_value=1, max_value=10, value=2)
    length_fullname = st.number_input("Full Name Length", min_value=1, max_value=100, value=15)
    name_equal_username = st.selectbox("Name equals Username?", [0, 1])
    description_length = st.number_input("Bio Description Length", min_value=0, max_value=1000, value=120)
    external_url = st.selectbox("Has External URL?", [0, 1])
    private = st.selectbox("Is Private Account?", [0, 1])
    posts = st.number_input("Number of Posts", min_value=0, max_value=10000, value=34)
    followers = st.number_input("Number of Followers", min_value=0, max_value=10000000, value=1000)
    follows = st.number_input("Number of Following", min_value=0, max_value=1000000, value=500)

    if st.button("Predict"):
        try:
            input_dict = {
                "profile pic": [profile_pic],
                "length_username": [length_username],
                "fullname words": [fullname_words],
                "length_fullname": [length_fullname],
                "name_edual_username": [name_equal_username],
                "description length": [description_length],
                "external URL": [external_url],
                "private": [private],
                "posts": [posts],
                "followers": [followers],
                "follows": [follows]
            }

            input_df = pd.DataFrame(input_dict)
            
            transformed = preprocess.transform(input_df)
            prediction = model.predict(transformed)[0]
            prediction_label = label_map[int(prediction)]

            st.success(f"🧠 Prediction: **{prediction_label}**")
        except Exception as e:
            st.error(f"Prediction failed: {e}")
