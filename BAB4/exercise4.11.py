my_pizzas = ["Pepperoni", "Cheese", "Margherita"]

friend_pizzas = my_pizzas[:]

my_pizzas.append("BBQ")
friend_pizzas.append("Hawaiian")

print("Pizza saya:")
for pizza in my_pizzas:
    print(pizza)

print("\nPizza teman saya:")
for pizza in friend_pizzas:
    print(pizza)