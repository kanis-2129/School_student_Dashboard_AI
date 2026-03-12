import streamlit as st

st.title("Teacher Portal")

menu = st.sidebar.selectbox(
    "Menu",
    ["Register","Login"]
)

# Register Page
if menu == "Register":

    st.subheader("Teacher Register")

    name = st.text_input("Name")
    email = st.text_input("Email")
    username = st.text_input("Username")
    password = st.text_input("Password",type="password")

    if st.button("Register"):

        st.success("Registration Successful")

# Login Page
elif menu == "Login":

    st.subheader("Teacher Login")

    username = st.text_input("Username")
    password = st.text_input("Password",type="password")

    if st.button("Login"):

        if username == "admin" and password == "1234":

            st.success("Login Successful")
            st.write("Welcome Teacher")

        else:

            st.error("Invalid login")
