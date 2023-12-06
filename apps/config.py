from textwrap import dedent

import streamlit as st


def display() -> None:
    st.set_page_config(
        page_title="Threading Demo",
        page_icon="🦘",
    )


    # FOR HIDE HEADER MENU: 
    #       [data-testid="stToolbar"] {visibility: hidden !important;}
    # FOR HIDE FOOTER MENU: 
    #       footer {visibility: hidden !important;}
    # hide_streamlit_style = dedent("""
    #     <style>
    #     [data-testid="stToolbar"] {visibility: hidden !important;}
    #     footer {visibility: hidden !important;}
    #     </style>
    # """)
    # st.markdown(hide_streamlit_style, unsafe_allow_html=True)