from time import sleep
from typing import Dict, Any

from app import BaseProcesser, BaseProcessersManager


class Processer1(BaseProcesser):
    def main_process(self, **kwargs) -> Dict[str, Any]:
        for i in range(3):
            sleep(1)
            print(i)
        return kwargs

    def pre_process(self, **kwargs) -> None:
        print("* PROCESSER 1")
        print("** START")

    def post_process(self, **kwargs) -> None:
        print("** FINISH")


class Processer2(BaseProcesser):
    def main_process(self, **kwargs) -> Dict[str, Any]:
        for i in range(3):
            sleep(1)
            print(i)
        return kwargs

    def pre_process(self, **kwargs) -> None:
        print("* PROCESSER 2")
        print("** START")

    def post_process(self, **kwargs) -> None:
        print("** FINISH")


class ProcesserList(BaseProcessersManager):
    def pre_process_for_starting(self, **kwargs) -> Dict[str, Any]:
        print("---- START ALL ----")
        return kwargs

    def pre_process_for_running(self) -> None:
        print("---- ERROR: RUNNING ----")

    def post_process(self) -> None:
        print("---- FINISH ALL ----")


processers = ProcesserList([Processer1, Processer2])
processers.run_all()
