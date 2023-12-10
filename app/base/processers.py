from abc import ABC, abstractmethod
from threading import Thread
from typing import List, Type, Dict, Any


class BaseProcesser(Thread, ABC):
    def __init__(self) -> None:
        super().__init__()

    @property
    def kwargs(self) -> Dict[str, Any]:
        return self.__kwargs
    
    def start_and_wait_to_complete(self, **kwargs) -> None:
        self.__kwargs = kwargs
        self.__kwargs = self.pre_process(**self.__kwargs)

        try:
            self.start()
        except RuntimeError:
            pass
        finally:
            self.join()

        self.__kwargs = self.post_process(**self.__kwargs)

    def run(self) -> None:
        self.__kwargs = self.main_process(**self.__kwargs)

    @abstractmethod
    def main_process(self, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def pre_process(self, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def post_process(self, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement this method")


class BaseProcessersManager(ABC):
    def __init__(self, processer_class_list: List[Type[BaseProcesser]]) -> None:
        self.__processer_class_list = processer_class_list
        self.__is_running = False

    @property
    def is_running(self) -> bool:
        return self.__is_running

    def run_all(self, **kwargs) -> None:
        is_running = self.__is_running

        # initialize processers if not running state
        if not is_running:
            self.init_processers()

        self.__is_running = True

        # run pre-process
        if is_running:
            kwargs = self.pre_process_for_running(**kwargs)
        else:
            kwargs = self.pre_process_for_starting(**kwargs)

        # run main-processes
        for processer in self.__processers:
            processer.start_and_wait_to_complete(**kwargs)
            kwargs = processer.kwargs

        # run post-process
        self.post_process(**kwargs)

        self.__is_running = False

    def init_processers(self) -> None:
        self.__processers = [processer_class() for processer_class in self.__processer_class_list]
        self.__is_running = False

    @abstractmethod
    def pre_process_for_starting(self, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def post_process(self, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement this method")
