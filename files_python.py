# Чтение файла recipes.txt
from pprint import pprint
with open("recipes.txt", "r", encoding="UTF-8") as job_file:
    dishes = {}
    for line in job_file:
        dish = line.strip()
        # print(dish)
        ingredients_n = int(job_file.readline())
        ingredients = []
        for _ in range(ingredients_n):
            string_ingredient = job_file.readline()
            string_ingredient = string_ingredient.strip()
            ingredient_name, quantity, measure = string_ingredient.split(" | ")
            ingredient = {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            ingredients.append(ingredient)
        job_file.readline()
        dishes[dish] = ingredients
pprint(dishes, sort_dicts=False)
