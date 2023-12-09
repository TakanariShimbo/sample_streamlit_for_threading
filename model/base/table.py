from abc import ABC, abstractmethod
from typing import List, Dict, Any, TypeVar, Generic, Type

import pandas as pd

from . import ColumnConfig
from . import BaseEntity


E = TypeVar("E", bound=BaseEntity)


class BaseTable(Generic[E], ABC):
    @classmethod
    def get_all_entities(cls) -> List[E]:
        table = cls.__get_table()
        return [cls.get_entiry_class()(series=row) for _, row in table.iterrows()]

    @classmethod
    def get_entity(cls, column_name: str, value: Any) -> E:
        table = cls.__get_table()
        mask = table.loc[:, column_name] == value
        matching_entities = table.loc[mask, :]
        if matching_entities.empty:
            raise ValueError(f"No rows found for {column_name}={value}")
        elif matching_entities.shape[0] > 1:
            raise ValueError(f"Multiple rows found for {column_name}={value}")
        return cls.get_entiry_class()(series=matching_entities.iloc[0])

    @classmethod
    def __get_table(cls) -> pd.DataFrame:
        if not hasattr(cls, "table"):
            cls.table = cls.__read_csv()
        return cls.table

    @classmethod
    def __read_csv(cls) -> pd.DataFrame:
        df = pd.read_csv(cls.get_filepath(), dtype=cls.__get_dtypes())
        cls.__validate(df)
        return df

    @classmethod
    def __get_dtypes(cls) -> Dict[str, Any]:
        return {column_config.name: column_config.dtype for column_config in cls.get_column_config_list()}

    @classmethod
    def __validate(cls, df: pd.DataFrame) -> None:
        for column_config in cls.get_column_config_list():
            if column_config.unique and df[column_config.name].duplicated().any():
                raise ValueError(f"Column {column_config.name} has duplicate values")
            if column_config.non_null and df[column_config.name].isnull().any():
                raise ValueError(f"Column {column_config.name} has null values")

    @staticmethod
    @abstractmethod
    def get_filepath() -> str:
        raise NotImplementedError("Subclasses must implement this method")

    @staticmethod
    @abstractmethod
    def get_column_config_list() -> List[ColumnConfig]:
        raise NotImplementedError("Subclasses must implement this method")

    @staticmethod
    @abstractmethod
    def get_entiry_class() -> Type[E]:
        raise NotImplementedError("Subclasses must implement this method")
