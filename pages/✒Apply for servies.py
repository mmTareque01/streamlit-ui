import streamlit as st

if "is_authenticated" not in st.session_state or not st.session_state["is_authenticated"]:

    with st.form("Sign Up"):

        st.text_input("User Name:", key="user_name")
        st.text_input("Organization Name:", key="orgranization_name")
        st.text_input("Email:", key="email")
        st.text_input("Phone:", key="phone")
        st.text_input("Password:", key="password", type="password")
        st.text_input("Confirm Password:", key='confirm_password', type="password")
        left, right = st.columns(2)
        with left:
            st.form_submit_button("Apply For Service")
        with right:
            st.markdown("[Already have an account? Login.](/)")
else:
    st.write("You are already a member of our family, thank you to be with us😍")
