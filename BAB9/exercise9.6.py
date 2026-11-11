class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print("Daftar rasa es krim:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Membuat objek
ice_cream = IceCreamStand(
    "Ice Cream House",
    "Dessert",
    ["Cokelat", "Vanila", "Stroberi", "Matcha"]
)

ice_cream.show_flavors()