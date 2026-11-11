from random import sample

lottery_items = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]

my_ticket = [1, "A", 5, "C"]

attempts = 0

while True:
    winning_ticket = sample(lottery_items, 4)
    attempts += 1

    if set(winning_ticket) == set(my_ticket):
        break

print("Tiket saya:", my_ticket)
print("Tiket pemenang:", winning_ticket)
print("Jumlah percobaan:", attempts)