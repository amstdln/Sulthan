from pathlib import Path

path = Path("Prokom1/Scripts/exercise10/alice.txt")

try:
    contents = path.read_text()

    # Menghitung kata the
    jumlah = contents.lower().count("the")

    print("Jumlah kata the:", jumlah)

    # Menghitung the yang diikuti spasi
    jumlah_spasi = contents.lower().count("the ")

    print("Jumlah kata the dengan spasi:", jumlah_spasi)

except FileNotFoundError:
    print("File tidak ditemukan.")