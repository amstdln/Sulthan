class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Baterai memiliki kapasitas {self.battery_size} kWh.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        else:
            range = 0

        print(f"Mobil dapat menempuh sekitar {range} mil.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")


# Membuat objek mobil listrik
my_car = ElectricCar("Nissan", "Leaf", 2024)

# Menampilkan informasi awal
my_car.describe_car()
my_car.battery.describe_battery()

# Menampilkan jarak tempuh sebelum upgrade
my_car.battery.get_range()

# Melakukan upgrade baterai
my_car.battery.upgrade_battery()

# Menampilkan hasil setelah upgrade
my_car.battery.describe_battery()
my_car.battery.get_range()