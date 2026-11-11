from random import sample

lottery_items = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]

winning_ticket = sample(lottery_items, 4)

print("Nomor undian yang menang:")
print(winning_ticket)

print("Tiket yang memiliki 4 angka atau huruf tersebut akan mendapatkan hadiah!")