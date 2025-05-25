import joblib
from preprocess import preprocess_skills

# Load models
kmeans = joblib.load("kmeans_model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

def predict_cluster(skills_text):
    cleaned = preprocess_skills(skills_text)
    vec = vectorizer.transform([cleaned])
    cluster = kmeans.predict(vec)[0]
    return cluster
