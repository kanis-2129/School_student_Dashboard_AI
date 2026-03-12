import streamlit as st

st.title("Teacher Portal")

# Session storage
if "registered_users" not in st.session_state:
    st.session_state.registered_users = {}

if "page" not in st.session_state:
    st.session_state.page = "register"

if "current_user" not in st.session_state:
    st.session_state.current_user = None


# ---------------- REGISTER PAGE ----------------
if st.session_state.page == "register":

    st.subheader("Teacher Register")

    name = st.text_input("Name", key="reg_name")
    email = st.text_input("Email", key="reg_email")
    username = st.text_input("Username", key="reg_username")
    password = st.text_input("Password", type="password", key="reg_password")

    if st.button("Register"):

        if username in st.session_state.registered_users:
            st.error("Username already exists")

        else:
            st.session_state.registered_users[username] = {
                "name": name,
                "email": email,
                "password": password
            }

            st.success("Registration Successful")

            st.session_state.page = "login"
            st.rerun()


# ---------------- LOGIN PAGE ----------------
elif st.session_state.page == "login":

    st.subheader("Teacher Login")

    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login"):

        users = st.session_state.registered_users

        if username in users and users[username]["password"] == password:

            st.session_state.current_user = username
            st.session_state.page = "home"
            st.rerun()

        else:
            st.error("Invalid Username or Password")


# ---------------- HOME PAGE ----------------
elif st.session_state.page == "home":

    username = st.session_state.current_user
    name = st.session_state.registered_users[username]["name"]

    st.success(f"Welcome {name} 👋")

    st.title("Teacher Home Page")

    st.write("You are successfully logged in.")

    if st.button("Logout"):
        st.session_state.page = "login"
        st.rerun()
