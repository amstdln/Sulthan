responses = {}

while True:
    name = input("Siapa nama kamu? ")
    place = input("Jika bisa berlibur ke mana saja, kamu ingin pergi ke mana? ")

    responses[name] = place

    repeat = input("Apakah ada orang lain yang ingin menjawab? (yes/no): ")

    if repeat.lower() == "no":
        break

print("\nHasil polling:")
for name, place in responses.items():
    print(f"{name} ingin berlibur ke {place}.")