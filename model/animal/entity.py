import pandas as pd

from .. import BaseEntity


class AnimalEntity(BaseEntity):
    def __init__(self, series: pd.Series):
        self.__key = series["key"]
        self.__filepath = series["filepath"]
        self.__label_en = series["label_en"]
        self.__label_jp = series["label_jp"]

    def key(self) -> str:
        return self.__key

    def filepath(self) -> str:
        return self.__filepath

    def label_en(self) -> str:
        return self.__label_en

    def label_jp(self) -> str:
        return self.__label_jp
