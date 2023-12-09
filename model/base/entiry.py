import pandas as pd


class BaseEntity:
    def __init__(self, series: pd.Series):
        raise NotImplementedError("Subclasses must implement this method")

