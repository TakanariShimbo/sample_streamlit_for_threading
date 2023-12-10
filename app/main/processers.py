from time import sleep

import cv2
import streamlit as st

from .schema import FormSchema
from .. import BaseProcesser, BaseProcessersManager


class Processer1(BaseProcesser):
    def main_process(self, **kwargs):
        for i in range(5):
            sleep(1)
            print(i)

    def pre_process(self, **kwargs):
        st.write("* PROCESSER 1")
        st.write("** START")
        print("* PROCESSER 1")
        print("** START")

    def post_process(self, **kwargs):
        st.write("** FINISH")
        print("** FINISH")


class Processer2(BaseProcesser):
    def main_process(self, **kwargs):
        for i in range(5):
            sleep(1)
            print(i)

    def pre_process(self, **kwargs):
        st.write("* PROCESSER 2")
        st.write("** START")
        print("* PROCESSER 2")
        print("** START")

    def post_process(self, **kwargs):
        st.write("** FINISH")
        print("** FINISH")


class ProcessersManager(BaseProcessersManager):
    def set_form_area(self, form_area):
        with form_area:
            self.__form_area = st.empty()

    def get_form_area(self):
        return self.__form_area

    def set_form_schema(self, form_schema: FormSchema):
        self.__form_schema = form_schema

    def get_form_schema(self) -> FormSchema:
        return self.__form_schema

    def pre_process_for_starting(self, **kwargs):
        self.set_form_area(form_area=kwargs["form_area"])
        self.set_form_schema(form_schema=kwargs["form_schema"])
        self.get_form_area().info("START")
        st.markdown("### Result")
        print("---- START ----")

    def pre_process_for_running(self, **kwargs):
        self.set_form_area(form_area=kwargs["form_area"])
        self.get_form_area().warning("RUNNING")
        st.markdown("### Result")
        print("---- RUNNING ----")

    def post_process(self, **kwargs):
        self.get_form_area().info("FINISH")
        st.image(
            image=cv2.imread(filename=self.get_form_schema().image_filepath),
            caption=self.get_form_schema().animal_type,
            channels="BGR",
        )
        st.balloons()
        print("---- FINISH ----")
