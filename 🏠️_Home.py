import streamlit as st
from others.remove_hamburger import remove_hamburger
from session_handler.login_session import login_session

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="⛄️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://mmtareque.com',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    },

)
def logout():
    del st.session_state["is_authenticated"]
def do_something():
    st.write("i am somtning")
    print(st.experimental_get_query_params)

remove_hamburger(st)


if "is_authenticated" not in st.session_state or not st.session_state["is_authenticated"]:

    login_session()
else:
    # st.set_page_config(
    #     page_title="Welcome to CT"
    # )
    st.write("this is home page")
    st.write("Here goes your normal Streamlit app...")
    st.button("Click me")

    with st.sidebar:
        st.button("do something", on_click=do_something)
        st.button("Log Out", on_click=logout)