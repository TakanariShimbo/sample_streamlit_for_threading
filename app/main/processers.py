from time import sleep

import streamlit as st

from .. import BaseProcesser, BaseProcessersManager


class Processer1(BaseProcesser):
    def main_process(self):
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
    def main_process(self):
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
    def set_message_area(self, form_area):
        with form_area:
            self.__message_area = st.empty()

    def get_message_area(self):
        return self.__message_area

    def pre_process_for_starting(self, **kwargs):
        self.set_message_area(form_area=kwargs["form_area"])
        self.get_message_area().info("START")
        st.markdown("### Result")
        print("---- START ----")

    def pre_process_for_running(self, **kwargs):
        self.set_message_area(form_area=kwargs["form_area"])
        self.get_message_area().warning("RUNNING")
        st.markdown("### Result")
        print("---- RUNNING ----")

    def post_process(self, **kwargs):
        self.get_message_area().info("FINISH")
        st.balloons()
        print("---- FINISH ----")