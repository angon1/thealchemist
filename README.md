# The Alchemist

The Alchemist is a simple alchemy engine designed for games and applications. It allows you to create ingredients, tools, products, and procedures to simulate alchemical processes.

## Features

- Ingredient creation and management
- Tool creation and usage
- Product creation through procedures
- Extendable and modular design

## Installation

### Building and Installing from GitHub

To download the source code from GitHub, build, and install locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone git@github.com:angon1/thealchemist.git
    ```

2. Navigate to the project directory:

    ```bash
    cd thealchemist
    ```

3. Build and install the package:

    ```bash
    pip install .
    ```

## Usage

```python
from the_alchemist.example_ingredient_app import ingredient_app

if __name__ == "__main__":
    ingredients = ingredient_app.get_all_ingredients()
    for ingredient in ingredients:
        print(ingredient)
```

License

## License

This project is licensed under the BSD 2-Clause License.
