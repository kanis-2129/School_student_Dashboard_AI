import streamlit as st
import logic
import plotly.express as px

# 1. Page Configuration (React style)
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
    menu = st.sidebar.radio("Navigate to:", ["🏠 Home Dashboard", "📤 Attendance Upload", "📝 Marks Entry", "🤖 AI Risk Insights", "⚙️ Settings"])
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Log Out"):
        st.session_state['logged_in'] = False
        st.rerun()

    # Dynamic Content based on Sidebar selection
   if st.session_state['logged_in']:
    menu = st.sidebar.radio("Navigate to:", ["🏠 Home Dashboard", "📤 Attendance Upload", "📝 Marks Entry", "🤖 AI Risk Insights"])

    if menu == "📤 Attendance Upload":
        st.title("📅 Monthly Attendance Management")
        file = st.file_uploader("Upload ERP Attendance", type=['xlsx', 'csv'])
        if file:
            # logic.py-la irukura function-a inga use panrom
            df_att = logic.process_attendance(file)
            st.session_state['att_data'] = df_att
            st.success("Attendance Processed!")
            st.dataframe(df_att)

    elif menu == "📝 Marks Entry":
        st.title("✍️ Student Marks Management")
        file = st.file_uploader("Upload Marks Sheet", type=['xlsx', 'csv'])
        if file:
            import pandas as pd
            df_marks = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)
            st.session_state['marks_data'] = df_marks
            st.success("Marks Uploaded!")

    elif menu == "🤖 AI Risk Insights":
        st.title("🤖 AI-Driven Performance Prediction")
        if 'att_data' in st.session_state and 'marks_data' in st.session_state:
            # Logic file-la irundhu AI result-a fetch panrom
            final_df = logic.get_ai_risk(st.session_state['att_data'], st.session_state['marks_data'])
            st.dataframe(final_df[['Student_Name', 'Attendance_%', 'HalfYearly_Marks', 'AI_Result']])
            
            fig = px.scatter(final_df, x="Attendance_%", y="HalfYearly_Marks", color="AI_Result", hover_name="Student_Name")
            st.plotly_chart(fig)
        else:
            st.warning("Please upload both Attendance and Marks data first!")
