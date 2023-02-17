from biautom.game.chip import Chip

class Place():
    def __init__(self) -> None:
        self.content: dict[Chip,tuple[int,int]]
    
    def place(self, chip: Chip, position: tuple[int, int]):
        self.content.update({ chip : position })
