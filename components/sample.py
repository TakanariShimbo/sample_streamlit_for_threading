from time import sleep

import streamlit as st

from handlers.processers import BaseProcesser, BaseProcesserList


class Processer1(BaseProcesser):
    def run(self):
        sleep(5)

    def pre_process(self):
        st.write("* PROCESSER 1")
        st.write("** START")

    def post_process(self):
        st.write("** FINISH")


class Processer2(BaseProcesser):
    def run(self):
        sleep(5)

    def pre_process(self):
        st.write("* PROCESSER 2")
        st.write("** START")

    def post_process(self):
        st.write("** FINISH")


class ProcesserList(BaseProcesserList):
    def pre_process_for_starting(self):
        self.message_area = st.empty()
        self.message_area.info("START")

    def pre_process_for_running(self):
        self.message_area = st.empty()
        self.message_area.warning("ALREADY STARTED")

    def post_process(self):
        self.message_area.info("FINISH")


PROCESSER_LIST_STATE = "PROCESSER_LIST_STATE"
def init_session_state():
    if not PROCESSER_LIST_STATE in st.session_state:
        st.session_state[PROCESSER_LIST_STATE] = ProcesserList([Processer1, Processer2])

def display():
    init_session_state()

    if st.button(label="RUN"):
        with st.container():
            st.session_state[PROCESSER_LIST_STATE].run_all()