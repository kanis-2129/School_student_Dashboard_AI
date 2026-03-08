import streamlit as st
import logic  # Namma separate logic file
import plotly.express as px
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="AI School ERP Dashboard", layout="wide", initial_sidebar_state="expanded")

# 2. Modern UI CSS Styling
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3em; background-color: #4A90E2; color: white; border: none; }
    .stButton>button:hover { background-color: #357ABD; border: none; }
    .sidebar .sidebar-content { background-color: #2c3e50; color: white; }
    .metric-card {
        background-color: white; padding: 20px; border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-top: 5px solid #4A90E2;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Session State for Login
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- PAGE 1: LOGIN ---
if not st.session_state['logged_in']:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.markdown("<br><br><h1 style='text-align: center; color: #4A90E2;'>🏫 School AI ERP</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Teacher Portal Login</p>", unsafe_allow_html=True)
        with st.container():
            u = st.text_input("Username")
            p = st.text_input("Password", type="password")
            if st.button("Sign In"):
                if u == "admin" and p == "school123":
                    st.session_state['logged_in'] = True
                    st.rerun()
                else:
                    st.error("Invalid Username or Password")

# --- PAGE 2: MAIN DASHBOARD ---
else:
    # Sidebar Navigation Menu
    st.sidebar.markdown("<h2 style='text-align: center;'>Admin Menu</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    
    # Unified Menu (Duplicate remove pannittaen)
    menu = st.sidebar.radio("Navigate to:", ["🏠 Home Dashboard", "📤 Attendance Upload", "📝 Marks Entry", "🤖 AI Risk Insights"])
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Log Out"):
        st.session_state['logged_in'] = False
        st.rerun()

    # Dynamic Content
    if menu == "🏠 Home Dashboard":
        st.title("📊 School Academic Overview")
        m1, m2, m3, m4 = st.columns(4)
        with m1: st.markdown("<div class='metric-card'><h4>Total Students</h4><h2>120</h2></div>", unsafe_allow_html=True)
        with m2: st.markdown("<div class='metric-card'><h4>Avg Attendance</h4><h2>92%</h2></div>", unsafe_allow_html=True)
        with m3: st.markdown("<div class='metric-card'><h4>Pass Rate</h4><h2>85%</h2></div>", unsafe_allow_html=True)
        with m4: st.markdown("<div class='metric-card'><h4>Risk Alerts</h4><h2 style='color:red;'>12</h2></div>", unsafe_allow_html=True)
        st.info("Welcome back! Please upload data in the sidebar to generate AI reports.")

    elif menu == "📤 Attendance Upload":
        st.title("📅 Monthly Attendance Management")
        st.info("Upload the ERP sheet with 1 to 31 date columns.")
        file = st.file_uploader("Upload ERP Attendance", type=['xlsx', 'csv'])
        if file:
            # logic.py-la irukura process_attendance function-a call panrom
            df_att = logic.process_attendance(file)
            st.session_state['att_data'] = df_att
            st.success("Attendance Processed Successfully!")
            st.dataframe(df_att)

    elif menu == "📝 Marks Entry":
        st.title("✍️ Student Marks Management")
        file = st.file_uploader("Upload Marks Sheet (Student_Name, Quarterly_Marks, HalfYearly_Marks)", type=['xlsx', 'csv'])
        if file:
            df_marks = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)
            st.session_state['marks_data'] = df_marks
            st.success("Marks Data Uploaded!")
            st.dataframe(df_marks)

    elif menu == "🤖 AI Risk Insights":
        st.title("🤖 AI-Driven Performance Prediction")
        if 'att_data' in st.session_state and 'marks_data' in st.session_state:
            # logic.py-la irukura get_ai_risk function-a call panrom
            final_df = logic.get_ai_risk(st.session_state['att_data'], st.session_state['marks_data'])
            
            st.subheader("AI Analysis Table")
            st.dataframe(final_df[['Student_Name', 'Attendance_%', 'HalfYearly_Marks', 'AI_Result']])
            
            st.subheader("Visual Risk Mapping")
            fig = px.scatter(final_df, x="Attendance_%", y="HalfYearly_Marks", color="AI_Result", 
                             hover_name="Student_Name", size_max=60, title="Student Performance Risk Graph")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Please upload both Attendance and Marks data first to see AI insights.")
