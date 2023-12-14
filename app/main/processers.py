from time import sleep
from typing import Dict, Any

import cv2
import streamlit as st

from .schema import FormSchema
from .. import BaseProcesser, BaseProcessersManager, EarlyStopProcessException


class Processer1(BaseProcesser):
    def main_process(self, **kwargs) -> Dict[str, Any]:
        sleep(3)
        kwargs["filepath"] = kwargs["form_schema"].image_filepath
        kwargs["animal_type"] = kwargs["form_schema"].animal_type
        kwargs["image_discription"] = kwargs["form_schema"].image_discription
        return kwargs

    def pre_process(self, **kwargs) -> None:
        st.markdown("### Result")

        st.write("* PROCESSER 1")
        st.write("** START")

    def post_process(self, **kwargs) -> None:
        st.write("** FINISH")


class Processer2(BaseProcesser):
    def main_process(self, **kwargs) -> Dict[str, Any]:
        sleep(3)
        kwargs["image"] = cv2.imread(filename=kwargs["filepath"], flags=cv2.IMREAD_COLOR)
        return kwargs

    def pre_process(self, **kwargs) -> None:
        st.write("* PROCESSER 2")
        st.write("** START")

    def post_process(self, **kwargs) -> None:
        st.write("** FINISH")


class ProcessersManager(BaseProcessersManager):
    def pre_process_for_starting(self, **kwargs) -> Dict[str, Any]:
        with kwargs["form_area"]:
            kwargs["message_area"] = st.empty()

        try:
            kwargs["form_schema"] = FormSchema.from_entity(animal_entity=kwargs["animal_entity"], image_discription=kwargs["image_discription"])
        except:
            kwargs["message_area"].warning("Please input form corectly.")
            raise EarlyStopProcessException()

        kwargs["message_area"].info("START")
        return kwargs

    def pre_process_for_running(self, **kwargs) -> None:
        with kwargs["form_area"]:
            kwargs["message_area"] = st.empty()
        kwargs["message_area"].warning("RUNNING")

    def post_process(self, **kwargs) -> None:
        kwargs["message_area"].info("FINISH")
        st.image(
            image=kwargs["image"],
            caption=f"{kwargs['animal_type']}: {kwargs['image_discription']}",
            channels="BGR",
        )
        st.balloons()
