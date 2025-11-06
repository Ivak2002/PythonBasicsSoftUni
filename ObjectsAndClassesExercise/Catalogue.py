class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [p for p in self.products if p.startswith(first_letter)]

    def __repr__(self):
        items = sorted(self.products)
        return "Items in the {} catalogue:\n{}".format(
            self.name,
            "\n".join(items)
        )
