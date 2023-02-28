from __future__ import annotations

from biautom.game.chip import Chip


class Placement:
    def __init__(self, position: tuple[int, int], top: Placement|None = None, bot: Placement|None = None, left: Placement|None = None, right: Placement|None = None) -> None:
        self.position : tuple[int, int] = position
        if not top is None:
            top.bot = self
        self.top: Placement | None = top

        if not bot is None:
            bot.top= self
        self.bot: Placement | None = bot

        if not left is None:
            left.right= self
        self.left: Placement | None = left

        if not right is None:
            right.left= self
        self.right: Placement | None = right

    def delete(self) -> None:
        if not self.top is None:
            self.top.bot = self.bot
        if not self.bot is None:
            self.bot.top = self.top
        if not self.left is None:
            self.left.right = self.right
        if not self.right is None:
            self.right.left = self.left
        del self
        return None

class Place:
    def __init__(self) -> None:
        self.content: dict[tuple[int, int], Chip] = {}
        self.structure: dict[Chip, Placement] = {}

    def place(self, position: tuple[int, int], chip: Chip) -> bool:
        if self.content.get(position, None) is None:
            self.content.update({position: chip})
            
            top_of: list[int] = [item[1] for item in self.content.keys() if item[0]==position[0] and item[1]>position[1]]
            bot_of: list[int] = [item[1] for item in self.content.keys() if item[0] == position[0] and item[1]<position[1]]
            left_of: list[int] = [item[0] for item in self.content.keys() if item[1] == position[1] and item[0]<position[0]]
            right_of: list[int] = [item[0] for item in self.content.keys() if item[1] == position[1] and item[0]>position[0]]

            top = None
            if top_of!=[]:
                top = self.structure[self.content[(position[0],min(top_of))]]
            bot = None
            if bot_of!=[]:
                bot = self.structure[self.content[(position[0],max(bot_of))]]
            left = None
            if left_of!=[]:
                left = self.structure[self.content[(max(left_of), position[1])]]
            right = None
            if right_of!=[]:
                right = self.structure[self.content[(min(right_of), position[1])]]

            self.structure.update({chip: Placement(position, top = top, bot = bot, left = left, right = right)})
            return True
        return False
