from pathlib import Path

path = Path("Prokom1/Scripts/exercise10/learning_python.txt")

# Membaca seluruh isi file
contents = path.read_text()
print("Membaca seluruh isi file:")
print(contents)

# Membaca file dan menyimpan baris ke dalam list
lines = contents.splitlines()

print("Membaca file menggunakan perulangan:")
for line in lines:
    print(line)