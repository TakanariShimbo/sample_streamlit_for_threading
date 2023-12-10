from time import sleep

import cv2
import streamlit as st

from .. import BaseProcesser, BaseProcessersManager


class Processer1(BaseProcesser):
    def main_process(self, **kwargs):
        for i in range(5):
            sleep(1)
            print(i)
        kwargs["filepath"] = kwargs["form_schema"].image_filepath
        kwargs["animal_type"] = kwargs["form_schema"].animal_type
        return kwargs

    def pre_process(self, **kwargs):
        st.write("* PROCESSER 1")
        st.write("** START")
        print("* PROCESSER 1")
        print("** START")
        return kwargs

    def post_process(self, **kwargs):
        st.write("** FINISH")
        print("** FINISH")
        return kwargs


class Processer2(BaseProcesser):
    def main_process(self, **kwargs):
        for i in range(5):
            sleep(1)
            print(i)
        kwargs["image"] = cv2.imread(filename=kwargs["filepath"])
        return kwargs

    def pre_process(self, **kwargs):
        st.write("* PROCESSER 2")
        st.write("** START")
        print("* PROCESSER 2")
        print("** START")
        return kwargs

    def post_process(self, **kwargs):
        st.write("** FINISH")
        print("** FINISH")
        return kwargs


class ProcessersManager(BaseProcessersManager):
    def pre_process_for_starting(self, **kwargs):
        with kwargs["form_area"]:
            kwargs["message_area"] = st.empty()
        kwargs["message_area"].info("START")
        st.markdown("### Result")
        print("---- START ----")
        return kwargs

    def pre_process_for_running(self, **kwargs):
        with kwargs["form_area"]:
            kwargs["message_area"] = st.empty()
        kwargs["message_area"].warning("RUNNING")
        st.markdown("### Result")
        print("---- RUNNING ----")
        return kwargs

    def post_process(self, **kwargs):
        kwargs["message_area"].info("FINISH")
        st.image(
            image=kwargs["image"],
            caption=kwargs["animal_type"],
            channels="BGR",
        )
        st.balloons()
        print("---- FINISH ----")
