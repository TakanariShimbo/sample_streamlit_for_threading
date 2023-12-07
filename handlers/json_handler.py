import json


class JsonHandler:
    @staticmethod
    def load(filepath) -> str:
        with open(filepath, "r") as f:
            return json.load(f)