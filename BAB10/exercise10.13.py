from pathlib import Path
import json

user = {}

user["nama"] = input("Masukkan nama: ")
user["umur"] = input("Masukkan umur: ")
user["kota"] = input("Masukkan kota: ")

# Menyimpan data ke file
path = Path("user_data.json")

contents = json.dumps(user)
path.write_text(contents)

# Membaca kembali data dari file
saved_contents = path.read_text()
saved_user = json.loads(saved_contents)

# Menampilkan informasi pengguna
print("\nInformasi pengguna:")
print(f"Nama: {saved_user['nama']}")
print(f"Umur: {saved_user['umur']}")
print(f"Kota: {saved_user['kota']}")