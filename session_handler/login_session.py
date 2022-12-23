from login.login_form import login_form
import streamlit as st

def login_session():
    """Returns `True` if the user had the correct password."""
    if "is_authenticated" not in st.session_state:
        login_form()
        return False
    elif not st.session_state["is_authenticated"]:
        login_form()
        st.error("😕 Password incorrect")
        return False
    else:
        return True
