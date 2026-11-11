from pathlib import Path

path = Path("guest_book.txt")

while True:
    name = input("Masukkan nama Anda (ketik quit untuk berhenti): ")

    if name == "quit":
        break

    with path.open(mode="a") as file:
        file.write(name + "\n")

    print(f"Selamat datang, {name}!")

print("Daftar tamu berhasil disimpan.")