import json
from time import sleep
from textwrap import dedent

from streamlit_lottie import st_lottie

from .s_states import WakeupSState
from .. import BaseComponent


def load_jsonfile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


STREAMLIT_LOGO_LOTTIE = load_jsonfile("./static/lotties/streamlit_logo.json")


class WakeupComponent(BaseComponent):    
    @staticmethod
    def init() -> None:
        pass

    @staticmethod
    def main() -> None:
        st_lottie(STREAMLIT_LOGO_LOTTIE, key="STREAMLIT_LOGO_LOTTIE", speed=1.1, reverse=False, loop=False)
        sleep(4)
        WakeupSState.compolete_wakeup()


