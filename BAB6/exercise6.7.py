person1 = {
    "first_name": "Andi",
    "last_name": "Pratama",
    "age": 18,
    "city": "Surakarta"
}

person2 = {
    "first_name": "Budi",
    "last_name": "Santoso",
    "age": 19,
    "city": "Yogyakarta"
}

person3 = {
    "first_name": "Citra",
    "last_name": "Lestari",
    "age": 18,
    "city": "Semarang"
}

people = [person1, person2, person3]

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print()