from biautom.game.chip_reader import ChipReader
from typing import Dict


class Chip:
    chip_data: dict = {}

    def __init__(self, name: str) -> None:
        self.name = name
