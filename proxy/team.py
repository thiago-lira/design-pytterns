from manager import Manager


class Team:
    def __init__(self):
        self.manager = Manager()

    def hire_player(self):
        is_player_available = self.manager.is_available()
        if is_player_available:
            print('Jogador está disponível para contratação. Vamos contratá-lo!')
        else:
            print('Jogador ainda tem contrato com outro time.')
