from abc import abstractmethod, ABCMeta


class Ingredient(metaclass=ABCMeta):
    @abstractmethod
    def description(self):
        pass


class Calabresa(Ingredient):
    def description(self):
        return 'Rodelas de calabresa trazida diretamente da Moóca, meô.'


class Onion(Ingredient):
    def description(self):
        return 'Rodelas de cebolas; de chorar...'


class Dough(Ingredient):
    def description(self):
        return 'Massa super gostosa'


class TomatoSauce(Ingredient):
    def description(self):
        return 'Molho de tomate'


class Mozzarella(Ingredient):
    def description(self):
        return 'Queijo feito do leite de vaquinhas virgens.'


class Oregano(Ingredient):
    def description(self):
        return 'Para dar aquele cheirinho e gostinho especial à pizza.'
