from abc import ABC, abstractmethod
from textwrap import dedent

import streamlit as st


class BasePage(ABC):        
    @classmethod
    def display(cls) -> None:
        cls.set_config(title=cls.get_title(), icon=cls.get_icon())
        cls.init()
        cls.main()

    @staticmethod
    def set_config(title: str, icon: str) -> None:
        st.set_page_config(
            page_title=title,
            page_icon=icon,
        )

        # FOR HIDE HEADER MENU:
        #       [data-testid="stToolbar"] {visibility: hidden !important;}
        # FOR HIDE FOOTER MENU:
        #       footer {visibility: hidden !important;}
        hide_streamlit_style = dedent(
            """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
        """
        )
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    @staticmethod
    @abstractmethod
    def get_title() -> str:
        raise NotImplementedError("Subclasses must implement this method")
    
    @staticmethod
    @abstractmethod
    def get_icon() -> str:
        raise NotImplementedError("Subclasses must implement this method")
    
    @staticmethod
    @abstractmethod
    def init() -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @staticmethod
    @abstractmethod
    def main() -> None:
        raise NotImplementedError("Subclasses must implement this method")