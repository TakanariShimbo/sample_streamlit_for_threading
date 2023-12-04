from abc import ABC, abstractmethod
from threading import Thread
from typing import List, Type


class BaseProcesser(Thread, ABC):
    def __init__(self) -> None:
        super().__init__()

    def start_and_wait_to_complete(self):
        self.pre_process()

        try:
            self.start()
        except RuntimeError as e:
            pass
        finally:
            self.join()

        self.post_process()

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def pre_process(self):
        pass

    @abstractmethod
    def post_process(self):
        pass


class BaseProcesserList(ABC):
    def __init__(self, processer_class_list: List[Type[BaseProcesser]]) -> None:
        self.__processer_class_list = processer_class_list
        self.__processers = self.__init_processers(self.__processer_class_list)

        self.__is_running = False

    @property
    def is_running(self):
        return self.__is_running

    def run_all(self):
        # initialize processers if not running state
        if not self.__is_running:
            self.__processers = self.__init_processers(self.__processer_class_list)

        # run pre-process
        if self.__is_running:
            self.pre_process_for_running()
        else:
            self.pre_process_for_starting()

        # run main-processes
        self.__is_running = True
        for processer in self.__processers:
            processer.start_and_wait_to_complete()
        self.__is_running = False

        # run post-process
        self.post_process()

    @staticmethod
    def __init_processers(processer_class_list: List[Type[BaseProcesser]]) -> List[BaseProcesser]:
        return [processer_class() for processer_class in processer_class_list]

    @abstractmethod
    def pre_process_for_starting(self):
        pass

    @abstractmethod
    def pre_process_for_running(self):
        pass

    @abstractmethod
    def post_process(self):
        pass
