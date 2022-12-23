import  streamlit as st

def login_controller():
    """Checks whether a password entered by the user is correct."""
    # print(len(st.session_state["email"]) == 0)
    if len(st.session_state["email"]) == 0:
        st.warning("Email is empty")
        # st.stop()
    if st.session_state["password"] == "123" and st.session_state["email"] == "tareque":
        st.session_state["is_authenticated"] = True
        del st.session_state["password"]  # don't store password
    else:
        st.session_state["is_authenticated"] = False
