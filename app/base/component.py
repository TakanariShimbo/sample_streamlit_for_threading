from abc import ABC, abstractmethod


class BaseComponent(ABC):
    @staticmethod
    @abstractmethod
    def init() -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @staticmethod
    @abstractmethod
    def main() -> None:
        raise NotImplementedError("Subclasses must implement this method")
        
    @classmethod
    def display(cls) -> None:
        cls.init()
        cls.main()
