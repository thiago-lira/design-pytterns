from random import randint


class Bingo:
    def __init__(self):
        self.observers = []
        self.number = None
        self.is_game_over = False
        self.available_numbers = [x+1 for x in range(99)]

    def draw_number(self):
        if not len(self.available_numbers):
            self.is_game_over = True

        number_drawn = randint(1, 99)
        is_number_already_drawn = not number_drawn in self.available_numbers
        if not is_number_already_drawn:
            self.available_numbers.remove(number_drawn)
            self.number = number_drawn
            self.dispatch()
        else:
            self.draw_number()

    def attach_player(self, card):
        self.observers.append(card)

    def dispatch(self):
        number = self.number
        for observer in self.observers:
            observer.update(number)
