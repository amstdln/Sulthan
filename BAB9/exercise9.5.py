class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Email: {self.email}")


# Membuat objek pengguna
user = User("Andi", "Saputra", 20, "andi@gmail.com")

# Menambah percobaan login
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Menampilkan jumlah percobaan login
print("Jumlah percobaan login:", user.login_attempts)

# Mengatur ulang percobaan login
user.reset_login_attempts()

# Menampilkan hasil setelah direset
print("Jumlah percobaan login setelah reset:", user.login_attempts)