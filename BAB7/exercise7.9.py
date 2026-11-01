sandwich_orders = [
    "tuna", "pastrami", "beef",
    "pastrami", "chicken", "pastrami"
]

finished_sandwiches = []

print("Deli kehabisan pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Sandwich {sandwich} sudah dibuat.")
    finished_sandwiches.append(sandwich)

print("\nSandwich yang sudah dibuat:")
for sandwich in finished_sandwiches:
    print(sandwich)