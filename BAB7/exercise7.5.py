while True:
    age = input("Masukkan usia (ketik 'quit' untuk berhenti): ")

    if age == "quit":
        break

    age = int(age)

    if age < 3:
        print("Tiket gratis.")
    elif age <= 12:
        print("Harga tiket $10.")
    else:
        print("Harga tiket $15.")