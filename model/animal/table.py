from typing import List

import pandas as pd

from .. import ColumnConfig, BaseTable


class AnimalTable(BaseTable):
    @staticmethod
    def get_filepath() -> str:
        return "./model/animal/data.csv"

    @staticmethod
    def get_column_config_list() -> List[ColumnConfig]:
        return [
            ColumnConfig(name="id", dtype=pd.Int64Dtype(), unique=True, non_null=True),
            ColumnConfig(name="value", dtype=pd.StringDtype(), unique=True, non_null=True),
            ColumnConfig(name="label_en", dtype=pd.StringDtype(), unique=True, non_null=True),
            ColumnConfig(name="label_jp", dtype=pd.StringDtype(), unique=True, non_null=True),
        ]
