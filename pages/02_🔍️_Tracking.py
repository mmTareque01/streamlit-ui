import streamlit as st
from session_handler.login_session import login_session


if "is_authenticated" not in st.session_state or not st.session_state["is_authenticated"]:

    login_session()
else:
    st.write("thi si for live vdoe")