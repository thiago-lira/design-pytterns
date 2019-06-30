from bingo import Bingo
from player import Player


if __name__ == '__main__':
    bingo = Bingo()
    p1 = Player('José', [1, 2, 5, 6, 7], bingo)
    p2 = Player('Maria', [18, 9, 2, 7, 3], bingo)
    p3 = Player('João', [15, 26, 78, 9, 1], bingo)
    bingo.attach_player(p1)
    bingo.attach_player(p2)

    while not bingo.is_game_over:
        bingo.draw_number()
