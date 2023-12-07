from textwrap import dedent

import streamlit as st

from .. import BasePage, MainComponent, WakeupComponent, WakeupSState


class HomePage(BasePage):    
    @staticmethod
    def init() -> None:
        WakeupSState.init()

    @staticmethod
    def main() -> None:
        if WakeupSState.get():
            WakeupComponent.display()
            st.rerun()

        MainComponent.display()