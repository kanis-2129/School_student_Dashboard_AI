import streamlit as st

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
    if menu == "🏠 Home Dashboard":
        st.title("📊 School Academic Overview")
        st.write("Overview of performance across all classes.")
        
        # UI Metric Cards (React look)
        m1, m2, m3, m4 = st.columns(4)
        with m1: st.markdown("<div class='metric-card'><h4>Total Students</h4><h2>1,250</h2></div>", unsafe_allow_html=True)
        with m2: st.markdown("<div class='metric-card'><h4>Average Attendance</h4><h2>94%</h2></div>", unsafe_allow_html=True)
        with m3: st.markdown("<div class='metric-card'><h4>Pass Percentage</h4><h2>88%</h2></div>", unsafe_allow_html=True)
        with m4: st.markdown("<div class='metric-card'><h4>AI Risk Alerts</h4><h2 style='color:red;'>15</h2></div>", unsafe_allow_html=True)

    elif menu == "📤 Attendance Upload":
        st.title("📅 Monthly Attendance Management")
        st.info("Please upload the ERP generated attendance Excel sheet below.")
        st.file_uploader("Drop Attendance Excel here", type=['xlsx', 'csv'])

    elif menu == "📝 Marks Entry":
        st.title("✍️ Student Marks Management")
        st.selectbox("Select Exam Type", ["Quarterly", "Half-Yearly", "Unit Test", "Assignments"])
        st.file_uploader("Upload Marks Sheet", type=['xlsx', 'csv'])

    elif menu == "🤖 AI Risk Insights":
        st.title("🤖 AI-Driven Performance Prediction")
        st.warning("Data connection pending. Please upload Attendance & Marks to see AI analysis.")
