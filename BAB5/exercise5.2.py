# File: conditional_tests.py

# 1. Tes untuk kesetaraan (equality) dan ketidaksamaan (inequality) dengan string
food = 'pizza'
print("Is food == 'pizza'? I predict True.")
print(food == 'pizza')

print("\nIs food != 'burger'? I predict True.")
print(food != 'burger')

# 2. Tes menggunakan metode lower()
car = 'Audi'
print("\nIs car.lower() == 'audi'? I predict True.")
print(car.lower() == 'audi')

print("\nIs car.lower() == 'bmw'? I predict False.")
print(car.lower() == 'bmw')

# 3. Tes numerik (kesetaraan, ketidaksamaan, lebih besar, lebih kecil, dll.)
age = 25
print(f"\nTesting with age = {age}")
print("Is age == 25? True:", age == 25)
print("Is age != 30? True:", age != 30)
print("Is age > 20? True:", age > 20)
print("Is age < 18? False:", age < 18)
print("Is age >= 25? True:", age >= 25)
print("Is age <= 24? False:", age <= 24)

# 4. Tes menggunakan kata kunci 'and' dan 'or'
x = 10
y = 20
print(f"\nTesting with x = {x} and y = {y}")
print("Is x > 5 and y > 15? True:", x > 5 and y > 15)
print("Is x > 15 or y > 15? True:", x > 15 or y > 15)

# 5. Tes apakah suatu item ada di dalam list (menggunakan 'in')
colors = ['red', 'green', 'blue']
print("\nIs 'green' in colors? True:", 'green' in colors)
print("Is 'yellow' in colors? False:", 'yellow' in colors)

# 6. Tes apakah suatu item tidak ada di dalam list (menggunakan 'not in')
print("\nIs 'yellow' not in colors? True:", 'yellow' not in colors)
print("Is 'red' not in colors? False:", 'red' not in colors)