from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    unique_ingredients = set(dish_ingredients)
    return (dish_name, unique_ingredients)
print(clean_ingredients('Punjabi-Style Chole', ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro']))


def check_drinks(drink_name, drink_ingredients):
    drink_ingredients2 = set(drink_ingredients)
    for ingredient in drink_ingredients2:
        if ingredient not in ALCOHOLS:
            return drink_name + " Mocktail"
        else:
            return drink_name + " Cocktail"
print(check_drinks('Honeydew Cucumber', ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber']))

