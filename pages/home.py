elif st.session_state.page == "home":

    username = st.session_state.current_user
    name = st.session_state.registered_users[username]["name"]

    st.title("🏫 School AI ERP")

    st.success(f"Welcome {name} 👋")

    st.write("Teacher Dashboard")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📅 Attendance Upload"):
            st.write("Attendance page coming soon")

    with col2:
        if st.button("📝 Marks Entry"):
            st.write("Marks page coming soon")

    with col3:
        if st.button("🤖 AI Risk Prediction"):
            st.write("AI page coming soon")

    st.divider()

    if st.button("Logout"):
        st.session_state.page = "login"
        st.rerun()
