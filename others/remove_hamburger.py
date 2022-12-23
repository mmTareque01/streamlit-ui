def remove_hamburger(st):
    hide_menu_style = """
            <style>
            .e1pxm3bq0{visibility: hidden;}
            .egzxvld0 {visibility: hidden;}
            
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    # MainMenu {visibility: hidden;}