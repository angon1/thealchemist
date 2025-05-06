from ..models.feature_based_recipe import FeatureBasedRecipe
from ..models.specific_ingredients_recipe import SpecificIngredientsRecipe


registered_recipe_types = {
    "feature_based": FeatureBasedRecipe,
    "specific_ingredients": SpecificIngredientsRecipe,
}

registered_recipes = {
    "Healing Potion": {
        "recipe_type": "feature_based",  # Changed from 'type' to 'recipe_type'
        "required_feature": "healing",
        "category": "potion",
        "product": "Healing Potion",
        "minimum_skills_level": {"alchemy": 2},
        "modifiers": {"healing": 5},
    },
    "Relaxation Ointment": {
        "recipe_type": "specific_ingredients",  # Changed from 'type' to 'recipe_type'
        "ingredients": ["Lavender", "Rosemary"],
        "category": "ointment",
        "product": "Relaxation Ointment",
        "minimum_skills_level": {"alchemy": 3},
        "modifiers": {"aroma": 2},
        "product_data": {
            "category": "ointment",
            "name": "Relaxation Ointment",
            "features": {"aroma": 10, "healing": 2},
        },
    },
}