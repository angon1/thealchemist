from products.mixture import Mixture

registered_product_types = {
    "mixture": Mixture,
}

HEALING_POTION_KEY = "Healing Potion"

registered_recipes = {
    "Healing Potion": {
        "name": "Healing Potion",
        "description": "A potion that heals wounds and restores health.",
        "category": "mixture",
        "features": {"healing": 0},
        },
}
