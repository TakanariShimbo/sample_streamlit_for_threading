from abc import ABC, abstractmethod


class BaseComponent(ABC):
    @staticmethod
    @abstractmethod
    def display() -> None:
        raise NotImplementedError("Subclasses must implement this method")
