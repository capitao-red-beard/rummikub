import game
import player


p1 = player.Player('Jasper')
p2 = player.Player('Damares')

g = game.Game([p1, p2])

# print(g.players)
# print(g.pot_tiles._tiles)

g.give_random_tile(p1)
print(g.players)
print(p1.tiles)
