import streamlit as st
import pandas as pd
from predict import predict_cluster

st.title("🧠 Job Cluster Predictor")

user_input = st.text_area("Enter your skills (e.g. Python, Machine Learning, SQL):")

if st.button("Predict Cluster"):
    if user_input:
        cluster = predict_cluster(user_input)
        st.success(f"✅ Your profile matches Cluster #{cluster}")
        
        df = pd.read_csv("clustered_jobs.csv")
        matches = df[df["Cluster"] == cluster][["Title", "Company", "Location", "Skills"]]
        
        st.write(f"### 🔍 Jobs in your cluster ({len(matches)} found):")
        st.dataframe(matches)
    else:
        st.warning("Please enter some skills first.")
