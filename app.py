import streamlit as st
import pandas as pd
import pickle
import numpy as np
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import requests
import os

# 1. Page Config (MUST be the very first Streamlit command)
st.set_page_config(page_title="CreditShield AI Pro", page_icon="🏦", layout="wide")

# 2. Asset Loaders
def load_lottieurl(url):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except: return None

@st.cache_resource
def load_model_assets():
    # Check if files exist first to prevent NameError
    if not os.path.exists('model.pkl') or not os.path.exists('mappings.pkl'):
        return None, None
    
    try:
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('mappings.pkl', 'rb') as f:
            mappings = pickle.load(f)
        return model, mappings
    except:
        return None, None

model, mappings = load_model_assets()
lottie_fin = load_lottieurl("https://lottie.host/8636e0d3-37a5-472d-8869-90d2e85a0695/S9iB6jY16p.json")

# 3. Corrected CSS (Removed the 'stdio' error)
st.markdown("""
    <style>
    .stApp { background: #f0f2f6; }
    div.stButton > button {
        background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%) !important;
        color: #1e1e1e !important;
        border: none !important;
        font-weight: bold !important;
        height: 3.5rem !important;
        border-radius: 12px !important;
    }
    </style>
    """, unsafe_allow_html=True) # Fixed: Removed unsafe_allow_stdio

# 4. Header & Safety Logic
if model is None or mappings is None:
    st.error("⚠️ System Files Missing!")
    st.info("Please run your Jupyter Notebook ('brain' file) to generate 'model.pkl' and 'mappings.pkl' in this folder.")
    st.stop()

# 5. UI Layout
st.markdown("<h1 style='text-align: center;'>🛡️ CreditShield Intelligence</h1>", unsafe_allow_html=True)

m1, m2, m3 = st.columns(3)
m1.metric("Model Engine", "Decision Tree")
m2.metric("Accuracy", "92%")
m3.metric("Status", "Live / Secure")

col1, col2 = st.columns([1, 1.5], gap="large")

with col1:
    st.subheader("📝 Applicant Details")
    age = st.number_input("Age", 18, 95, 25)
    income = st.number_input("Annual Income ($)", 0, 1000000, 50000)
    home = st.selectbox("Home Ownership", list(mappings['person_home_ownership'].values()))
    emp_len = st.slider("Work Experience (Years)", 0, 40, 5)
    intent = st.selectbox("Loan Purpose", list(mappings['loan_intent'].values()))
    grade = st.select_slider("Credit Grade", options=list(mappings['loan_grade'].values()))
    amount = st.number_input("Loan Amount ($)", 0, 50000, 10000)
    rate = st.number_input("Interest Rate (%)", 0.0, 25.0, 11.0)
    default = st.radio("Prior Default?", list(mappings['cb_person_default_on_file'].values()), horizontal=True)
    hist = st.number_input("Credit History (Years)", 1, 40, 5)

def get_key(val, dictionary):
    for key, value in dictionary.items():
        if val == value: return key
    return 0

with col2:
    st.subheader("📊 Analysis Result")
    if st.button("🚀 ANALYZE RISK"):
        features = np.array([[
            age, income, get_key(home, mappings['person_home_ownership']),
            float(emp_len), get_key(intent, mappings['loan_intent']),
            get_key(grade, mappings['loan_grade']), amount, rate,
            (amount / income if income > 0 else 0),
            get_key(default, mappings['cb_person_default_on_file']), hist
        ]])
        
        prediction = model.predict(features)
        prob = model.predict_proba(features)[0]
        confidence = prob[0] if prediction[0] == 0 else prob[1]
        
        if prediction[0] == 0:
            st.success("### ✅ VERDICT: LOW RISK / APPROVED")
            st.balloons()
        else:
            st.error("### ❌ VERDICT: HIGH RISK / REJECTED")

        # Visual Gauge
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = confidence * 100,
            title = {'text': "Confidence Score (%)"},
            gauge = {'bar': {'color': "#2ecc71" if prediction[0]==0 else "#e74c3c"}}
        ))
        st.plotly_chart(fig, use_container_width=True)
    else:
        if lottie_fin: st_lottie(lottie_fin, height=300)