from time import sleep

from streamlit_lottie import st_lottie

from .s_states import WakeupSState
from .. import BaseComponent
from handler.json_handler import JsonHandler


class WakeupComponent(BaseComponent):
    STREAMLIT_LOGO = JsonHandler.load("./static/lotties/streamlit_logo.json")

    @classmethod
    def init(cls) -> None:
        pass

    @classmethod
    def main(cls) -> None:
        st_lottie(cls.STREAMLIT_LOGO, key="STREAMLIT_LOGO_LOTTIE", speed=1.2, reverse=False, loop=False)
        sleep(4)
        WakeupSState.compolete_wakeup()
