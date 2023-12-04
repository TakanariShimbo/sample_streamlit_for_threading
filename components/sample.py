from time import sleep

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
    def __add_message_area(self):
        self.__message_area = st.empty()

    def pre_process_for_starting(self):
        self.__add_message_area()
        self.__message_area.info("START")
        print("---- START ----")

    def pre_process_for_running(self):
        self.__add_message_area()
        self.__message_area.warning("ALREADY STARTED")
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
    def on_click_run(cls) -> None:
        cls.get().run_all()


def display():
    ProcessersManagerSState.init()

    if st.button(label="RUN"):
        ProcessersManagerSState.on_click_run()
