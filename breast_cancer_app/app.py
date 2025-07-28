import streamlit as st
import numpy as np
import pickle

# Load model and scaler
with open("breast_cancer_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Top 10 features used in the model
top_10_features = [
    "worst texture",
    "radius error",
    "worst symmetry",
    "mean concave points",
    "worst radius",
    "worst concavity",
    "worst concave points",
    "worst area",
    "area error",
    "mean concavity"
]

feature_stats = {
    "worst texture": (12.02, 49.54, 25.68),
    "radius error": (0.11, 2.87, 0.40),
    "worst symmetry": (0.16, 1.06, 0.66),
    "mean concave points": (0.00, 0.20, 0.03),
    "worst radius": (7.93, 36.04, 16.27),
    "worst concavity": (0.00, 1.25, 0.27),
    "worst concave points": (0.00, 0.29, 0.11),
    "worst area": (185.2, 4254.0, 880.6),
    "area error": (6.80, 542.20, 40.34),
    "mean concavity": (0.00, 0.43, 0.09)
}


# App title
st.set_page_config(page_title="Breast Cancer Predictor", layout="centered")
st.title("🔬 Breast Cancer Detection")
st.markdown("To predict whether the tumor is **Benign** or **Malignant**.")

# Two-column layout for inputs
col1, col2 = st.columns(2)
user_input = []

for i, feature in enumerate(top_10_features):
    with (col1 if i < 5 else col2):
        value = st.number_input(f"{feature.title()}", step=0.01, key=feature)
        user_input.append(value)

# Prediction button
if st.button("🧪 Diagnose"):
    try:
        input_array = scaler.transform([user_input])
        result = model.predict(input_array)[0]
        prediction = "Benign" if result == 1 else "Malignant"

        st.success(f"🔍 **Prediction:** {prediction}")
        if prediction == "Benign":
            st.success("✅ You're fine! The tumor is **not cancerous**.")
        else:
            st.error("⚠️ Please consult a doctor. The tumor **may be cancerous**.")

    except Exception as e:
        st.error(f"An error occurred: {e}")

# Sidebar reference
st.sidebar.title("📊 Feature Reference")

for feature, (min_val, max_val, mean_val) in feature_stats.items():
    st.sidebar.markdown(
        f"**{feature.capitalize()}**  \n"
        f"- Min: `{min_val}`  \n"
        f"- Max: `{max_val}`  \n"
        f"- Mean: `{mean_val}`  \n"
    )
