from factory_method.pizza import PizzaFactory
from factory_method.ingredient import (Onion, Mozzarella as MozzarellaCheese,
                                Calabresa as CalabresaIngredient, Oregano)


class Mozzarella(PizzaFactory):
    def specifics_ingredients(self):
        self.ingredients.append(MozzarellaCheese())
        self.ingredients.append(Oregano())

    def description(self):
        return 'Tradicional pizza da família tradicional (ou não) paulistana.'


class Calabresa(PizzaFactory):
    def specifics_ingredients(self):
        self.ingredients.append(CalabresaIngredient())
        self.ingredients.append(Onion())

    def description(self):
        return 'Segunda pizza no coração do paulistano.'
