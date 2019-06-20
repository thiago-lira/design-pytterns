from abc import ABCMeta, abstractmethod
from factory_method.ingredient import Dough, TomatoSauce

class PizzaFactory(metaclass=ABCMeta):
    def __init__(self):
        self.ingredients = []
        self.set_ingredients()

    def default_ingredients(self):
        self.ingredients.append(Dough())
        self.ingredients.append(TomatoSauce())

    def set_ingredients(self):
        self.default_ingredients()
        self.specifics_ingredients()

    @abstractmethod
    def specifics_ingredients(self):
        pass

    @abstractmethod
    def description(self):
        pass

    def show_details(self):
        ingredients = self.ingredients
        print(self.description())
        for ingredient in ingredients:
            index = ingredients.index(ingredient) + 1
            print("%i - %s" % (index, ingredient.description()))
