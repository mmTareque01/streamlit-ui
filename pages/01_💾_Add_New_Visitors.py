import streamlit as st
from session_handler.login_session import login_session

if "is_authenticated" not in st.session_state or not st.session_state["is_authenticated"]:
    login_session()
    # st.write("Please Login First...")
else:
    st.write("Take Picture and Input Detials About the Person")
    picture = st.camera_input("Take Picture")
    if picture:
        st.image(picture)

    with st.form("Add New Person"):
        left, right = st.columns(2)

        with left:
            st.text_input("Full Name:", key="full_name")
            st.text_input("Whatsapp:", key="whatsapp")
            st.text_input("text", key="unknow1")
            st.radio(
                "Gender:",
                ["Male", "Female"],
                key="visibility",
                # label_visibility=st.session_state.visibility,
                # disabled=st.session_state.disabled,
                horizontal=True,
            )

            # st.text_input("text")

        with right:
            st.text_input("Email:", key="email")
            st.text_input("Phone:", key="phone")
            st.text_input("text", key="unknow2")
            st.text_input("text", key="unknow3")
        st.text_area("About More", key='about_more')
        st.form_submit_button("Add")