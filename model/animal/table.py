from typing import List, Type

import pandas as pd

from .entity import AnimalEntity
from .. import ColumnConfig, BaseTable


class AnimalTable(BaseTable[AnimalEntity]):
    @staticmethod
    def get_filepath() -> str:
        return "./model/animal/data.csv"

    @staticmethod
    def get_column_config_list() -> List[ColumnConfig]:
        return [
            ColumnConfig(name="key", dtype=pd.StringDtype(), unique=True, non_null=True),
            ColumnConfig(name="filepath", dtype=pd.StringDtype(), unique=True, non_null=True),
            ColumnConfig(name="label_en", dtype=pd.StringDtype(), unique=True, non_null=True),
            ColumnConfig(name="label_jp", dtype=pd.StringDtype(), unique=True, non_null=True),
        ]
    
    @staticmethod
    def get_entiry_class() -> Type[AnimalEntity]:
        return AnimalEntity
