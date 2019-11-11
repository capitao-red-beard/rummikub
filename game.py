import tile
import random


class Game:

    def __init__(self, players):
        self._players = players
        self._pot_tiles = tile.RummikubTiles()
    
    @property
    def players(self):
        return self._players
    
    @property
    def pot_tiles(self):
        return self._pot_tiles
    
    def give_random_tile(self, player):
        player.tiles.append(random.choice(self._pot_tiles))
