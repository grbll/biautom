from biautom.game.place import StructuredPlace
from biautom.game.place import Place


class Player:
    def __init__(self,player_name : str) -> None:
        self.name: str = player_name
        self.field: StructuredPlace = StructuredPlace()
        self.bag: Place = Place() 
