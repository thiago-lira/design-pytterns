from card import Card


class Player(Card):
    def __init__(self, name, numbers, publisher):
        self.name = name
        self.numbers = numbers
        self.publisher = publisher

    def player_has_number(self, number):
        has_number = number in self.numbers
        if has_number:
            self.numbers.remove(number)
        return has_number

    def is_winner(self):
        return len(self.numbers) == 0

    def update(self, number):
        if self.player_has_number(number) and self.is_winner():
            self.publisher.is_game_over = True
            print(self.name, 'gritou "Bingo!"')
