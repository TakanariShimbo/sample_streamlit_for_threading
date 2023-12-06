from abc import ABC, abstractmethod
from threading import Thread
from typing import List, Type


class BaseProcesser(Thread, ABC):
    def __init__(self) -> None:
        super().__init__()

    def start_and_wait_to_complete(self) -> None:
        self.pre_process()

        try:
            self.start()
        except RuntimeError:
            pass
        finally:
            self.join()

        self.post_process()

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def pre_process(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def post_process(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")


class BaseProcessersManager(ABC):
    def __init__(self, processer_class_list: List[Type[BaseProcesser]]) -> None:
        self.__processer_class_list = processer_class_list
        self.__is_running = False
        self.__called_count = 0

    @property
    def is_running(self) -> bool:
        return self.__is_running
    
    @property
    def called_count(self) -> int:
        return self.__called_count

    def run_all(self, **kwargs) -> None:
        # initialize processers if not running state
        if not self.__is_running:
            self.init_processers()

        # run pre-process
        if self.__is_running:
            self.pre_process_for_running(**kwargs)
        else:
            self.pre_process_for_starting(**kwargs)

        # run main-processes
        self.__is_running = True
        self.__called_count += 1
        for processer in self.__processers:
            processer.start_and_wait_to_complete()
        self.__is_running = False

        # run post-process
        self.post_process(**kwargs)

    def init_processers(self) -> None:
        self.__processers = [processer_class() for processer_class in self.__processer_class_list]
        self.__is_running = False
        self.__called_count = 0

    @abstractmethod
    def pre_process_for_starting(self, **kwargs) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def pre_process_for_running(self, **kwargs) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def post_process(self, **kwargs) -> None:
        raise NotImplementedError("Subclasses must implement this method")
