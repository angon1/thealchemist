from rich.pretty import pprint
from ingredients.factory.ingredient_factory import IngredientFactory


def main():
    herb_data = {
        "category": "herb",
        "name": "Mandrake",
        "description": "A root that looks like a human",
        "features": {"healing": 3},
    }

    pprint("Welcome to the alchemy world")
    factory = IngredientFactory()
    my_new_herb = factory.create(herb_data)
    pprint(f"Created a new herb: {my_new_herb}")
    pprint(f"Features: {my_new_herb.get_features()}")


if __name__ == "__main__":
    main()
