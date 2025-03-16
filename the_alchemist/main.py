from rich.pretty import pprint
from ingredients.ingredient_factory import IngredientFactory


herb_data = {
    "category": "herb",
    "name": "Mandrake",
    "description": "A root that looks like a human",
    "features": {"healing": 3},
}

if __name__ == "__main__":
    pprint("Welcome int the alchemy world")
    factory = IngredientFactory()
    my_new_herb = factory.produce_ingredient(herb_data)
    pprint(f"Created a new herb: {my_new_herb}")
    pprint(f"Features: {my_new_herb.get_features()}")
