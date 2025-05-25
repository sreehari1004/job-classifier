import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import joblib
from preprocess import preprocess_skills

# Load data
df = pd.read_csv("karkidi_jobs.csv")
df["Cleaned_Skills"] = df["Skills"].apply(preprocess_skills)

# Vectorize
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["Cleaned_Skills"])

# Clustering
kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(X)

# Save results
df["Cluster"] = clusters
df.to_csv("clustered_jobs.csv", index=False)

# Save model and vectorizer
joblib.dump(kmeans, "kmeans_model.joblib")
joblib.dump(vectorizer, "vectorizer.joblib")

print("Training complete and models saved.")
