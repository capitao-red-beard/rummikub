from collections import namedtuple


Player = namedtuple('Name', ['tiles'])


class Player:

    def __init__(self, name):
        self._name = name
        self._tiles = []

    @property
    def name(self):
        return self._name
    
    @property
    def tiles(self):
        return self._tiles

    @tiles.setter
    def tiles(self, tiles):
        self._tiles.append(tiles)
