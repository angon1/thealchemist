from products.mappings import registered_product_types

class ProductFactory:
    @staticmethod
    def create(data: dict):
        try:
            category = data.get("category", None)
            print(data)
            return registered_product_types.get(category)(**data)
        except Exception as e:
            raise Exception(f"Failed to create ingredient: {e}")
