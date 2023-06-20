# Resolvida com ajuda da monitoria, Chat GPT e Rodrigo Monteiro (25B)
import csv
from models.ingredient import Ingredient
from models.dish import Dish
from collections import defaultdict


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path, encoding="utf8") as file:
            menu_reader = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = menu_reader
        self.dishes = self.parse_data(data)

    def parse_data(self, data):
        recipes = defaultdict(list)  # para não dar KeyError
        for item in data:
            dish = item[0]
            price = float(item[1])
            ing_name = item[2]
            ing_qty = int(item[3])

            if dish not in recipes:
                recipes[dish] = Dish(dish, price)

            new_ing = Ingredient(ing_name)
            recipes[dish].add_ingredient_dependency(new_ing, ing_qty)
        return set(recipes.values())


# Obs.: o código abaixo NÃO funcionou para fazer o set de ingredientes:
# new_dish.add_ingredient_dependency(new_ing, ing_qty)
# recipes[dish].append(tuple(new_dish.recipe))
# Erro: Tipo lista não é hasheable
