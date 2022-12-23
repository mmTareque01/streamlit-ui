import streamlit as st
from login.login_controller import login_controller


def login_form():

    st.title("Login to continue...")
    with st.form("login_form"):
        st.text_input("Email:", key="email")
        st.text_input("Password:", key="password", type="password")
        st.form_submit_button("Login", on_click=login_controller)
        st.markdown("[Don't have account? Create One.](/Apply_for_servies)")

