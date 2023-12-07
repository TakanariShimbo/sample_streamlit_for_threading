from abc import ABC, abstractmethod


class BaseComponent(ABC):
    @classmethod
    def display(cls) -> None:
        cls.init()
        cls.main()

    @classmethod
    @abstractmethod
    def init(cls) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @classmethod
    @abstractmethod
    def main(cls) -> None:
        raise NotImplementedError("Subclasses must implement this method")
