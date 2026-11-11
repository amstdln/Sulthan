from pathlib import Path

filenames = ["Prokom1/Scripts/exercise10/cats.txt", "Prokom1/Scripts/exercise10/dogs.txt"]

for filename in filenames:
    path = Path(filename)

    try:
        contents = path.read_text()
        print(f"\nIsi file {filename}:")
        print(contents)

    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")