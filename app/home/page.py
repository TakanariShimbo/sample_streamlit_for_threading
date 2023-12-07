from textwrap import dedent

import streamlit as st

from .. import BasePage, MainComponent, WakeupComponent, WakeupSState


class HomePage(BasePage):    
    @classmethod
    def init(cls) -> None:
        WakeupSState.init()

    @classmethod
    def main(cls) -> None:
        if WakeupSState.get():
            WakeupComponent.display()
            st.rerun()

        MainComponent.display()