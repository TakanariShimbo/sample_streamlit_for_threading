from textwrap import dedent

import streamlit as st

from .s_states import ProcessersManagerSState
from .. import BasePage


class SamplePage(BasePage):
    @staticmethod
    def get_title() -> str:
        return "Threading Demo"
    
    @staticmethod
    def get_icon() -> str:
        return "🦘"
    
    @staticmethod
    def init() -> None:
        ProcessersManagerSState.init()

    @staticmethod
    def main() -> None:
        contents = dedent("""
            # Threading Demo  
            This demo is sample of using thread for managing process 🦘  
        """)
        st.markdown(contents)

        form_area = st.form(key="Form")
        with form_area:
            st.markdown("### Form")
            _, left_area, _, center_area, _, right_area, _ = st.columns([1,3,1,3,1,3,1])
            with left_area:
                is_run_pushed = st.form_submit_button(label="RUN", type="primary", use_container_width=True)
            with center_area:
                is_rerun_pushed = st.form_submit_button(label="RERUN", type="primary", use_container_width=True)
            with right_area:
                is_reset_pushed = st.form_submit_button(label="RESET", type="secondary", use_container_width=True)
        
        if is_run_pushed:
            ProcessersManagerSState.on_click_run(form_area=form_area)
        elif is_rerun_pushed:
            ProcessersManagerSState.on_click_rerun(form_area=form_area)
        elif is_reset_pushed:
            ProcessersManagerSState.on_click_reset()
