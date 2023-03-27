from __future__ import annotations

from biautom.game.chip import GameChip
from biautom.game.chip_data_handler import ChipDataHandler


class Place:
    def __init__(self) -> None:
        self.content: list[GameChip] = []

class StructuredPlace(Place):
    def __init__(self) -> None:
        self.structure: dict[tuple[int, int], GameChip] = {}
        self.columns: int = 0
        self.rows: int = 0

    def place(self, position: tuple[int, int], chip: GameChip) -> bool:
        if self.structure.get(position, None) is None:
            self.structure.update({position: chip})
            return True
        return False

    def remove(self, position: tuple[int, int]) -> GameChip|None:
        return self.structure.pop(position, None)

    def action(self, base_query: ChipDataHandler, current: GameChip, initial: GameChip) -> int:
        accumulated_value: int = 0
        self_check: bool = True

        if base_query.holds is not None:
            self_check = self_check and current.condition_check(base_query.holds, initial)
        if base_query.fails is not None:
            self_check = self_check and not current.condition_check(base_query.fails, initial)

        if self_check:
            position
        return accumulated_value
