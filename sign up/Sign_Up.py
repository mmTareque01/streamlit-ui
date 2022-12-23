import streamlit as st

st.title("Sign Up Page")


with st.form("Sign Up"):
    st.text_input("User Name", key="user_name")
    st.text_input("Organization Name:", key="orgranization_name")
    st.text_input("Email:", key="email")
    st.text_input("Phone:", key="phone")
    st.text_input("Password:", key="password", type="password")
    st.text_input("Confirm Password", key='confirm_password', type="password")
    st.form_submit_button("Apply For Service")