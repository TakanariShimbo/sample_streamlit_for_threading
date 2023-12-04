from typing import TypeVar, Generic
import abc

import streamlit as st


T = TypeVar("T")


class BaseSState(Generic[T], abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def get_name() -> str:
        raise NotImplementedError("Subclasses must implement this method")

    @staticmethod
    @abc.abstractmethod
    def get_default() -> T:
        raise NotImplementedError("Subclasses must implement this method")

    @classmethod
    def get(cls) -> T:
        return st.session_state[cls.get_name()]

    @classmethod
    def set(cls, value: T) -> None:
        st.session_state[cls.get_name()] = value

    @classmethod
    def reset(cls) -> None:
        cls.set(value=cls.get_default())

    @classmethod
    def init(cls) -> None:
        if not cls.get_name() in st.session_state:
            cls.reset()