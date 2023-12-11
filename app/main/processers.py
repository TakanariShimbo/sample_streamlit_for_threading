from time import sleep

import cv2
import streamlit as st

from .schema import FormSchema
from .. import BaseProcesser, BaseProcessersManager, EarlyStopProcessException


class Processer1(BaseProcesser):
    def main_process(self, **kwargs):
        for i in range(5):
            sleep(1)
            print(i)
        kwargs["filepath"] = kwargs["form_schema"].image_filepath
        kwargs["animal_type"] = kwargs["form_schema"].animal_type
        kwargs["image_discription"] = kwargs["form_schema"].image_discription
        return kwargs

    def post_process(self, **kwargs):
        st.write("** FINISH")
        print("** FINISH")

        st.write("* PROCESSER 2")
        st.write("** START")
        print("* PROCESSER 2")
        print("** START")
        return kwargs


class Processer2(BaseProcesser):
    def main_process(self, **kwargs):
        for i in range(5):
            sleep(1)
            print(i)
        kwargs["image"] = cv2.imread(filename=kwargs["filepath"], flags=cv2.IMREAD_COLOR)
        return kwargs

    def post_process(self, **kwargs):
        st.write("** FINISH")
        print("** FINISH")
        return kwargs


class ProcessersManager(BaseProcessersManager):
    def pre_process_for_starting(self, **kwargs):
        with kwargs["form_area"]:
            kwargs["message_area"] = st.empty()

        try:
            kwargs["form_schema"] = FormSchema.from_entity(animal_entity=kwargs["animal_entity"], image_discription=kwargs["image_discription"])
        except:
            kwargs["message_area"].warning("Please input form corectly.")
            raise EarlyStopProcessException()
        
        kwargs["message_area"].info("START")
        st.markdown("### Result")
        print("---- START ----")
        st.write("* PROCESSER 1")
        st.write("** START")
        print("* PROCESSER 1")
        print("** START")
        return kwargs

    def pre_process_for_running(self, **kwargs):
        with kwargs["form_area"]:
            kwargs["message_area"] = st.empty()
        kwargs["message_area"].warning("RUNNING")
        st.markdown("### Result")
        print("---- RUNNING ----")
        st.write("* PROCESSER 1")
        st.write("** START")
        print("* PROCESSER 1")
        print("** START")

    def post_process(self, **kwargs):
        kwargs["message_area"].info("FINISH")
        st.image(
            image=kwargs["image"],
            caption=f"{kwargs['animal_type']}: {kwargs['image_discription']}",
            channels="BGR",
        )
        st.balloons()
        print("---- FINISH ----")
