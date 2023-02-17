import biautom.misc.chipreader as chipreader
from typing import Dict


class Chip:
    chip_data = chipreader.load_all()

    def __init__(self, name: str) -> None:
        data: Dict = self.__class__.chip_data.get(
            name, self.__class__.chip_data.get("Default", {})
        )

        self.name = name
        self.type = data["type"]
