from abc import ABC, abstractmethod
from threading import Thread
from typing import List, Type, Dict, Any


class BaseProcesser(Thread, ABC):
    def __init__(self) -> None:
        super().__init__()

    def start_and_wait_to_complete(self, **kwargs) -> None:
        self._kwargs = kwargs
        self._kwargs = self.pre_process(**self._kwargs)

        try:
            self.start()
        except RuntimeError:
            pass
        finally:
            self.join()

        self._kwargs = self.post_process(**self._kwargs)

    def run(self) -> None:
        self._kwargs = self.main_process(**self._kwargs)

    @abstractmethod
    def pre_process(self, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def main_process(self, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def post_process(self, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement this method")


class EarlyStopProcessException(Exception):
    def __init__(self, message="Process stopped earlier than expected"):
        super().__init__(message)


class BaseProcessersManager(ABC):
    def __init__(self, processer_class_list: List[Type[BaseProcesser]]) -> None:
        self._processer_class_list = processer_class_list
        self._is_running = False

    def run_all(self, **kwargs) -> None:
        is_running = self._is_running
        self._is_running = True

        # run pre-process
        if not is_running:
            self._processers = [processer_class() for processer_class in self._processer_class_list]
            try:
                self._kwargs = self.pre_process_for_starting(**kwargs)
            except EarlyStopProcessException:
                self._is_running = is_running
                return
        else:
            self.pre_process_for_running(**kwargs)

        # run main-processes
        kwargs = self._kwargs
        for processer in self._processers:
            processer.start_and_wait_to_complete(**kwargs)
            kwargs = processer._kwargs

        # run post-process
        self.post_process(**kwargs)

        self._is_running = False

    def init_processers(self) -> None:
        self._processers = [processer_class() for processer_class in self._processer_class_list]
        self._is_running = False

    @abstractmethod
    def pre_process_for_starting(self, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def pre_process_for_running(self, **kwargs):
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def post_process(self, **kwargs):
        raise NotImplementedError("Subclasses must implement this method")
