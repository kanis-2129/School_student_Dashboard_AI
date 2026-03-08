import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Config & CSS
st.set_page_config(page_title="AI School ERP", layout="wide")
st.markdown("""<style>.main { background-color: #f4f7f6; } .stButton>button { background-color: #4A90E2; color: white; border-radius: 8px; }</style>""", unsafe_allow_html=True)

# 2. Login Logic
if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("🔐 Teacher Login")
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")
    if st.button("Login"):
        if u == "admin" and p == "school123":
            st.session_state['logged_in'] = True
            st.rerun()
else:
    # 3. Sidebar Menu
    menu = st.sidebar.radio("Menu", ["🏠 Dashboard Home", "📤 Upload Data", "🤖 AI Insights"])
    
    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False
        st.rerun()

    # --- HOME PAGE ---
    if menu == "🏠 Home Dashboard":
        st.title("📊 School Overview")
        st.info("Welcome! Go to 'Upload Data' to process school records.")

    # --- UPLOAD PAGE (Logic Starts Here) ---
    elif menu == "📤 Upload Data":
        st.title("📤 Data Integration")
        file = st.file_uploader("Upload Student Excel/CSV", type=['csv', 'xlsx'])
        if file:
            df = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)
            # Logic: Auto Attendance Calculation
            df['Attendance_%'] = (df['Present_Days'] / df['Total_Days']) * 100
            st.session_state['data'] = df
            st.success("Data Uploaded and Processed!")
            st.dataframe(df)

    # --- AI INSIGHTS PAGE (The Brain) ---
    elif menu == "🤖 AI Insights":
        if 'data' in st.session_state:
            df = st.session_state['data']
            st.title("🤖 AI Performance Prediction")
            
            # AI Logic: Risk Check
            def get_status(row):
                if row['Attendance_%'] < 75 or row['Marks'] < 40:
                    return "🔴 High Risk"
                return "🟢 Safe"
            
            df['AI_Status'] = df.apply(get_status, axis=1)
            st.write(df[['Student_Name', 'Attendance_%', 'Marks', 'AI_Status']])
            
            # Chart
            fig = px.bar(df, x="Student_Name", y="Marks", color="AI_Status", title="AI Student Analysis")
            st.plotly_chart(fig)
        else:
            st.warning("Please upload data first!")
