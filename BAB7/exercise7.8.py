sandwich_orders = ["tuna", "beef", "chicken"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Sandwich {sandwich} sudah dibuat.")

    finished_sandwiches.append(sandwich)

print("\nSandwich yang sudah dibuat:")
for sandwich in finished_sandwiches:
    print(sandwich)