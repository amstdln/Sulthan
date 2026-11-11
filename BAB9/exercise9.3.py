class User:
    def __init__(self, first_name, last_name, age, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city

    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Email: {self.email}")
        print(f"Kota: {self.city}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang.")


# Membuat beberapa objek pengguna
user1 = User("Sulthan", "Ahmad", 20, "Sulthan@gmail.com", "Surakarta")
user2 = User("Budi", "Hebat", 21, "budi@gmail.com", "Yogyakarta")
user3 = User("Citra", "Lestari", 19, "citra@gmail.com", "Semarang")

# Menampilkan informasi pengguna
user1.describe_user()
user1.greet_user()
print()

user2.describe_user()
user2.greet_user()
print()

user3.describe_user()
user3.greet_user()