from .processers import Processer1, Processer2, ProcessersManager
from .. import BaseSState


class ProcessersManagerSState(BaseSState[ProcessersManager]):
    @staticmethod
    def get_name() -> str:
        return "PROCESSERS_MANAGER"

    @staticmethod
    def get_default() -> ProcessersManager:
        return ProcessersManager([Processer1, Processer2])

    @classmethod
    def on_click_run(cls, form_area) -> None:
        processers_manager = cls.get()
        processers_manager.run_all(form_area=form_area)

    @classmethod
    def on_click_reset(cls) -> None:
        processers_manager = cls.get()
        processers_manager.init_processers()

    @classmethod
    def on_click_rerun(cls, form_area) -> None:
        processers_manager = cls.get()
        processers_manager.init_processers()
        processers_manager.run_all(form_area=form_area)
