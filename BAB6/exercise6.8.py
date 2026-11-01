pet1 = {"animal": "kucing", "owner": "Andi"}
pet2 = {"animal": "anjing", "owner": "Budi"}
pet3 = {"animal": "kelinci", "owner": "Citra"}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"Hewan: {pet['animal']}")
    print(f"Pemilik: {pet['owner']}\n")