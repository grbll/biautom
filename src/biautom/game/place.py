from __future__ import annotations

from biautom.game.chip import Chip


class Place:
    def __init__(self) -> None:
        self.content: dict[tuple[int, int], Chip] = {}


class StructuredPlace(Place):
    def __init__(self) -> None:
        self.content: dict[tuple[int, int], Chip] = {}

    def place(self, position: tuple[int, int], chip: Chip) -> bool:
        if self.content.get(position, None) is None:
            self.content.update({position: chip})
            return True
        return False

    def remove(self, position: tuple[int, int]) -> Chip|None:
        return self.content.pop(position, None)

class ControlledPlace(StructuredPlace):
    def place(self, position: tuple[int, int], chip: Chip) -> bool:
        if self.content.get(position, None) is None:
            self.content.update({position: chip})
            return True
        return False
