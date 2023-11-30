import os
from pprint import pprint


def add_new_cook_book() -> dict:
    """Add a new cookbook from recipes.txt."""
    recipes_book = {}
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    with open(file_path, encoding='UTF-8') as recipes:
        line = recipes.readline().strip()
        while line:
            recipes_book[line] = []
            for _ in range(int(recipes.readline().strip())):
                ingredient_property = recipes.readline().strip().split(' | ')
                recipes_book[line].append({
                    'ingredient_name': ingredient_property[0],
                    'quantity': int(ingredient_property[1]),
                    'measure': ingredient_property[2],
                })
            recipes.readline()
            line = recipes.readline().strip()
    return recipes_book


def get_shop_list_by_dishes(dishes: list, person_count: int):
    """Get a shopping list for a certain number of people."""
    shopping_dict = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shopping_dict:
                shopping_dict[ingredient['ingredient_name']] = {
                    'quantity': ingredient['quantity'] * person_count,
                    'measure': ingredient['measure']
                }
            else:
                shopping_dict[ingredient['ingredient_name']]['quantity'] += (
                        ingredient['quantity'] * person_count)
    pprint(shopping_dict)


cook_book = add_new_cook_book()

pprint(cook_book)
print()

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 5)
print()
get_shop_list_by_dishes(['Омлет', 'Салат'], 5)
