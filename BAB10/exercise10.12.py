from pathlib import Path
import json

path = Path("favorite_number.json")

if path.exists():
    contents = path.read_text()
    number = json.loads(contents)

    print(f"Saya tahu angka favorit Anda! Angkanya adalah {number}.")

else:
    number = input("Berapa angka favorit Anda? ")

    contents = json.dumps(number)
    path.write_text(contents)

    print("Angka favorit berhasil disimpan.")