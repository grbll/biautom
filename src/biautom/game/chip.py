from typing import Dict

from biautom.game.chip_data_handler import ChipDataHandler
from biautom.game.chip_reader import ChipReader


class Chip:

    def __init__(self, name: str) -> None:
        self.name : str = name
        
class GameChip(Chip):

    default_string = """
    {
      "family": [
        "*"
      ],
      "role": [
        "*"
      ],
      "placement": {
        "me": {
          "holds": {},
          "fails": {},
          "value": {
            "operation": "sum",
            "base" : 1
          },
          "positions": {},
          "loop": []
        }
      }
    }
    """
    game_chips= ChipReader(
        ["json/chip_data"],
        ["json/schemata"],
        ["json/schemata/chip_schema/chip_data.json"],
        default_string,
    )

    def __init__(self, name: str) -> None:
        super().__init__(name),
        self.data : dict = self.__class__.game_chips.chip_data.get(name,self.__class__.game_chips.default)

    def condition_check(self, condition: ChipDataHandler, initial : Chip) -> bool:
        check : bool = True
        if hasattr(condition, "initial"):
            check = check and (not condition.initial or self == initial)
        if hasattr(condition, "name"):
            check = check and ((self.name in condition.name) or ("*" in condition. name))
        if hasattr(condition, "kingdom"):
            check = check and ((self.kingdom in condition.kingdom) or ("*" in condition. kingdom))
        if hasattr(condition, "role"):
            check = check and ((self.role in condition.role) or ("*" in condition. role))
        return check
