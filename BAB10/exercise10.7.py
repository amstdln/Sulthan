while True:
    try:
        angka1 = input("Masukkan angka pertama (q untuk keluar): ")

        if angka1 == "q":
            break

        angka2 = input("Masukkan angka kedua: ")

        if angka2 == "q":
            break

        angka1 = int(angka1)
        angka2 = int(angka2)

        hasil = angka1 + angka2

        print("Hasil penjumlahan:", hasil)

    except ValueError:
        print("Maaf, masukkan angka yang benar!")

print("Program selesai.")