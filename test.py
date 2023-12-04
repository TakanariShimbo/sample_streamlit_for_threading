from time import sleep

from handlers.processers import BaseProcesser, BaseProcessersManager


class Processer1(BaseProcesser):
    def run(self):
        for i in range(5):
            sleep(1)
            print(i)

    def pre_process(self):
        print("* PROCESSER 1")
        print("** START")

    def post_process(self):
        print("** FINISH")


class Processer2(BaseProcesser):
    def run(self):
        for i in range(5):
            sleep(1)
            print(i)

    def pre_process(self):
        print("* PROCESSER 2")
        print("** START")

    def post_process(self):
        print("** FINISH")


class ProcesserList(BaseProcessersManager):
    def pre_process_for_starting(self):
        print("---- START ALL ----")

    def pre_process_for_running(self):
        print("---- ERROR: ALREADY STARTED ----")

    def post_process(self):
        print("---- FINISH ALL ----")


processers = ProcesserList([Processer1, Processer2])
processers.run_all()
