class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis makanan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka!")


# Membuat objek
restaurant = Restaurant("Warteg Kartika", "Masakan Indonesia")

# Menampilkan atribut
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Memanggil method
restaurant.describe_restaurant()
restaurant.open_restaurant()