from ingredients.db.mappings import registered_herbs, registered_ingredients
from ingredients.factory.ingredient_factory import IngredientFactory
from ingredients.repositories.herb_json_repository import HerbJsonRepository
from ingredients.service import IngredientService

# Example usage
if __name__ == "__main__":
    herb_repository = HerbJsonRepository()
    ingredient_factory = IngredientFactory(
        registered_ingredients=registered_ingredients
    )
    ingredient_service = IngredientService(
        ingredient_repository=herb_repository, ingredient_factory=ingredient_factory
    )

    # Adding a new herb
    new_herb_data = {
        "name": "Basil",
        "category": "herb",
        "description": "A fragrant herb used in cooking.",
        "properties": {"color": "green", "taste": "sweet"},
    }
    ingredient_service.add_ingredient(new_herb_data)
    for herb in registered_herbs.values():
        ingredient_service.add_ingredient(herb)

    # Getting all herbs
    all_herbs = ingredient_service.get_all_ingredients()
    print(all_herbs)


def create_service():
    """
    Create an instance of IngredientService with the necessary dependencies.
    """
    herb_repository = HerbJsonRepository()
    ingredient_factory = IngredientFactory(
        registered_ingredients=registered_ingredients
    )
    return IngredientService(
        ingredient_repository=herb_repository, ingredient_factory=ingredient_factory
    )


app = create_service()
