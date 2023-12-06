from abc import abstractmethod


class BaseComponent:
    @abstractmethod
    @staticmethod
    def display() -> None:
        raise NotImplementedError("Subclasses must implement this method")
