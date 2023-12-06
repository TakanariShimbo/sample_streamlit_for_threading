from .. import BaseSState


class WakeupSState(BaseSState[bool]):
    @staticmethod
    def get_name() -> str:
        return "WAKEUP"

    @staticmethod
    def get_default() -> bool:
        return True
    
    @classmethod
    def compolete_wakeup(cls) -> None:
        cls.set(value=False)