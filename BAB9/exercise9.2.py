class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis makanan: {self.cuisine_type}")


# Membuat tiga objek restoran
restaurant1 = Restaurant("Warteg Kartika", "Masakan Indonesia")
restaurant2 = Restaurant("Pizza Hut", "Makanan Italia")
restaurant3 = Restaurant("Sushi Hiro", "Makanan Jepang")

# Menampilkan informasi ketiga restoran
restaurant1.describe_restaurant()
print()

restaurant2.describe_restaurant()
print()

restaurant3.describe_restaurant()