from time import sleep
from textwrap import dedent

import streamlit as st

from handlers.processers import BaseProcesser, BaseProcessersManager
from handlers.s_states import BaseSState


class Processer1(BaseProcesser):
    def run(self):
        for i in range(5):
            sleep(1)
            print(i)

    def pre_process(self):
        st.write("* PROCESSER 1")
        st.write("** START")
        print("* PROCESSER 1")
        print("** START")

    def post_process(self):
        st.write("** FINISH")
        print("** FINISH")


class Processer2(BaseProcesser):
    def run(self):
        for i in range(5):
            sleep(1)
            print(i)

    def pre_process(self):
        st.write("* PROCESSER 2")
        st.write("** START")
        print("* PROCESSER 2")
        print("** START")

    def post_process(self):
        st.write("** FINISH")
        print("** FINISH")


class ProcessersManager(BaseProcessersManager):
    def set_form_area(self, form_area):
        self.__form_area = form_area

    def __add_message_area(self):
        with self.__form_area:
            self.__message_area = st.empty()

    def pre_process_for_starting(self):
        self.__add_message_area()
        self.__message_area.info("START")
        st.markdown("### Result")
        print("---- START ----")

    def pre_process_for_running(self):
        self.__add_message_area()
        self.__message_area.warning("ALREADY STARTED")
        st.markdown("### Result")
        print("---- ALREADY STARTED ----")

    def post_process(self):
        self.__message_area.info("FINISH")
        print("---- FINISH ----")


class ProcessersManagerSState(BaseSState[ProcessersManager]):
    @staticmethod
    def get_name() -> str:
        return "PROCESSERS_MANAGER"

    @staticmethod
    def get_default() -> ProcessersManager:
        return ProcessersManager([Processer1, Processer2])
    
    @classmethod
    def on_click_run(cls, form_area) -> None:
        processers_manager = cls.get()
        processers_manager.set_form_area(form_area=form_area)
        processers_manager.run_all()

    @classmethod
    def on_click_reset(cls, form_area) -> None:
        processers_manager = cls.get()
        processers_manager.set_form_area(form_area=form_area)
        processers_manager.init_processers()


def display_sample_contents():
    ProcessersManagerSState.init()

    contents = dedent("""
        # Threading Demo  
        This demo is sample of using thread for managing process 🦘  
    """)
    st.markdown(contents)

    form_area = st.form(key="Form")
    with form_area:
        st.markdown("### Form")
        _, left_area, _, right_area, _ = st.columns([1,3,1,3,1])
        with left_area:
            is_run_pushed = st.form_submit_button(label="RUN", use_container_width=True)
        with right_area:
            is_reset_pushed = st.form_submit_button(label="RESET", use_container_width=True)

    
    if is_run_pushed:
        ProcessersManagerSState.on_click_run(form_area=form_area)
    elif is_reset_pushed:
        ProcessersManagerSState.on_click_reset(form_area=form_area)
