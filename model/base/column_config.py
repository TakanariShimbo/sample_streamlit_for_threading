from pandas.api.extensions import ExtensionDtype


class ColumnConfig:
    def __init__(
        self,
        name: str,
        dtype: ExtensionDtype,
        unique: bool = False,
        non_null: bool = False,
    ):
        self.name = name
        self.dtype = dtype
        self.unique = unique
        self.non_null = non_null