import streamlit as st

st.title("Teacher Portal")

# Session storage
if "registered_users" not in st.session_state:
    st.session_state.registered_users = {}

if "page" not in st.session_state:
    st.session_state.page = "register"


# ---------------- REGISTER PAGE ----------------
if st.session_state.page == "register":

    st.subheader("Teacher Register")

    name = st.text_input("Name")
    email = st.text_input("Email")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):

        if username in st.session_state.registered_users:
            st.error("Username already exists")

        else:
            st.session_state.registered_users[username] = password
            st.success("Registration Successful")

            st.session_state.page = "login"
            st.rerun()


# ---------------- LOGIN PAGE ----------------
elif st.session_state.page == "login":

    st.subheader("Teacher Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        users = st.session_state.registered_users

        if username in users and users[username] == password:

            st.success("Login Successful")
            st.write("Welcome Teacher", username)

        else:
            st.error("Invalid Username or Password")
