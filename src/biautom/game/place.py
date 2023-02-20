from biautom.game.chip import Chip

class Place():
    def __init__(self) -> None:
        self.content: dict[tuple[int,int], Chip]
    
    def place(self, position: tuple[int, int], chip: Chip):
        if self.content.get(position, None) == None:
            self.content.update({position:chip})
