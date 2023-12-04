from abc import ABC, abstractmethod
from threading import Thread
from typing import List, Type


class BaseProcesser(Thread, ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def pre_process(self):
        pass

    @abstractmethod
    def post_process(self):
        pass

    def start_and_wait_to_complete(self):
        self.pre_process()

        try:
            self.start()
        except RuntimeError as e:
            pass
        finally:
            self.join()

        self.post_process()


class BaseProcesserList(ABC):
    def __init__(self, processer_class_list: List[Type[BaseProcesser]]) -> None:
        self.__processer_class_list = processer_class_list
        self.__processers = self.__init_processers(self.__processer_class_list)

        self.__is_running = False

    @abstractmethod
    def pre_process_for_starting(self):
        pass

    @abstractmethod
    def pre_process_for_running(self):
        pass

    @abstractmethod
    def post_process(self):
        pass

    @property
    def is_running(self):
        return self.__is_running

    @staticmethod
    def __init_processers(processer_class_list: List[Type[BaseProcesser]]) -> List[BaseProcesser]:
        return [processer_class() for processer_class in processer_class_list]

    def run_all(self):
        if not self.__is_running:
            self.__processers = self.__init_processers(self.__processer_class_list)

        if self.__is_running:
            self.pre_process_for_running()
        else:
            self.pre_process_for_starting()

        self.__is_running = True
        for processer in self.__processers:
            processer.start_and_wait_to_complete()
        self.__is_running = False

        self.post_process()



if __name__ == "__main__":
    from time import sleep

    class Processer1(BaseProcesser):
        def run(self):
            sleep(5)

        def pre_process(self):
            print("* PROCESSER 1")
            print("** START")

        def post_process(self):
            print("** FINISH")

    class Processer2(BaseProcesser):
        def run(self):
            sleep(5)

        def pre_process(self):
            print("* PROCESSER 2")
            print("** START")

        def post_process(self):
            print("** FINISH")

    class ProcesserList(BaseProcesserList):
        def pre_process_for_starting(self):
            print("---- START ALL ----")

        def pre_process_for_running(self):
            print("---- ERROR: ALREADY STARTED ----")

        def post_process(self):
            print("---- FINISH ALL ----")

    processers = ProcesserList([Processer1, Processer2])
    processers.run_all()
