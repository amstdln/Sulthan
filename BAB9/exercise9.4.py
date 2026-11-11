class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis makanan: {self.cuisine_type}")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

    
# Membuat objek restoran
restaurant = Restaurant("Warung Nusantara", "Masakan Indonesia")

# Menampilkan jumlah pelanggan awal
print("Jumlah pelanggan:", restaurant.number_served)

# Mengubah jumlah pelanggan
restaurant.number_served = 25
print("Jumlah pelanggan:", restaurant.number_served)

# Menggunakan method set_number_served()
restaurant.set_number_served(50)
print("Jumlah pelanggan:", restaurant.number_served)

# Menambahkan jumlah pelanggan
restaurant.increment_number_served(20)
print("Jumlah pelanggan:", restaurant.number_served)