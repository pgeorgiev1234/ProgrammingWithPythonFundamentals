class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        list1 = []
        for x in self.products:
            if x[0] == first_letter:
                list1.append(x)
        return list1

    def __repr__(self):
        self.products.sort()
        out = "Items in the Furniture catalogue:\n"
        out += "\n".join(self.products)
        return out

