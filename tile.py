from collections import namedtuple

Tile = namedtuple('Tile', ['value', 'color'])

class RummikubTile:
    values = [str(n) for n in range(1, 14)]
    colors = 'red blue orange black'.split()

    def __init__(self):
        self._tiles = [Tile(value, color) for color in self.colors
                                          for value in self.values]

    def __len__(self):
        return len(self._tiles)

    def __getitem__(self, position):
        return self._tiles[position]

rummikub_tiles = RummikubTile()

for tile in rummikub_tiles._tiles:
    print(tile)
