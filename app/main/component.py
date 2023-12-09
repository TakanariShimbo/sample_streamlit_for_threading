from textwrap import dedent

import streamlit as st

from .schema import FormSchema
from .s_states import ProcessersManagerSState
from .. import BaseComponent
from model import AnimalTable


class MainComponent(BaseComponent):
    @classmethod
    def init(cls) -> None:
        ProcessersManagerSState.init()

    @classmethod
    def main(cls) -> None:
        contents = dedent(
            """
            # Threading Demo  
            This demo is sample of using thread for managing process 🦘  
            """
        )
        st.markdown(contents)

        form_area = st.form(key="Form")
        with form_area:
            st.markdown("### Form")

            selected_animal_entity = st.selectbox(
                label="Animal Type", 
                options=AnimalTable.get_all_entities(),
                format_func= lambda enetity: enetity.label_en,
                key="AnimalTypeSelectBox",
            )

            _, left_area, _, center_area, _, right_area, _ = st.columns([1, 3, 1, 3, 1, 3, 1])
            with left_area:
                is_run_pushed = st.form_submit_button(label="RUN", type="primary", use_container_width=True)
            with center_area:
                is_rerun_pushed = st.form_submit_button(label="RERUN", type="primary", use_container_width=True)
            with right_area:
                is_reset_pushed = st.form_submit_button(label="RESET", type="secondary", use_container_width=True)

        if is_run_pushed:
            if not selected_animal_entity:
                return
            form_schema = FormSchema.from_entity(animal_entity=selected_animal_entity)
            ProcessersManagerSState.on_click_run(form_area=form_area, form_schema=form_schema)
        elif is_rerun_pushed:
            if not selected_animal_entity:
                return
            form_schema = FormSchema.from_entity(animal_entity=selected_animal_entity)
            ProcessersManagerSState.on_click_rerun(form_area=form_area, form_schema=form_schema)
        elif is_reset_pushed:
            ProcessersManagerSState.on_click_reset()
