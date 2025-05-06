from ..models.herb import Herb

registered_ingredients = {"herb": Herb}


registered_herbs = {
    "Rosemary": {
        "category": "herb",
        "name": "Rosemary",
        "description": "A fragrant herb used in cooking and medicine.",
        "features": {"flavor": 5, "healing": 3},
    },
    "Mandrake": {
        "category": "herb",
        "name": "Mandrake",
        "description": "A root that looks like a human",
        "features": {"healing": 3},
    },
}
