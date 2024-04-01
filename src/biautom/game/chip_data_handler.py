from  typing import Any

class ChipDataHandler:
    def __init__(self, /, **kwargs) -> None:
        self.__dict__ = kwargs
    
    def __getattr__(self, __name: str) -> Any:
        return self.__dict__.get(__name, None)

    def __str__(self) -> str:
        return str(self.__dict__)
