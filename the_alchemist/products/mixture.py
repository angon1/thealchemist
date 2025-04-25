from products.base_product import BaseProduct

class Mixture(BaseProduct):
    """
    A Mixture is a product that is created by combining multiple ingredients.
    It can have its own unique properties and features based on the ingredients used.
    """

    def consume(self):
        """
        Consumes the mixture and returns:
            - a message indicating the consumption
            - extra effects based on the mixture's features
        """
        return f"You have consumed the {self.name}."

