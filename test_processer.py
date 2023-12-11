from time import sleep

from app import BaseProcesser, BaseProcessersManager


class Processer1(BaseProcesser):
    def main_process(self, **kwargs):
        for i in range(3):
            sleep(1)
            print(i)
        return kwargs

    def pre_process(self, **kwargs):
        print("* PROCESSER 1")
        print("** START")

    def post_process(self, **kwargs):
        print("** FINISH")


class Processer2(BaseProcesser):
    def main_process(self, **kwargs):
        for i in range(3):
            sleep(1)
            print(i)
        return kwargs

    def pre_process(self, **kwargs):
        print("* PROCESSER 2")
        print("** START")

    def post_process(self, **kwargs):
        print("** FINISH")


class ProcesserList(BaseProcessersManager):
    def pre_process_for_starting(self, **kwargs):
        print("---- START ALL ----")
        return kwargs

    def pre_process_for_running(self):
        print("---- ERROR: RUNNING ----")

    def post_process(self):
        print("---- FINISH ALL ----")


processers = ProcesserList([Processer1, Processer2])
processers.run_all()
