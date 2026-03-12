import streamlit as st

def show_home():

    username = st.session_state.current_user
    name = st.session_state.registered_users[username]["name"]

    st.title("🏫 School AI ERP")

    st.success(f"Welcome {name} 👋")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("📅 Attendance Upload")

    with col2:
        st.button("📝 Marks Entry")

    with col3:
        st.button("🤖 AI Risk Prediction")
