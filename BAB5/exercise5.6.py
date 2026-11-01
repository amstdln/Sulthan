# Daftar umur dipakai agar semua cabang if-elif-else teruji sekaligus
for age in [1, 3, 10, 15, 30, 70]:
    if age < 2:
        stage = "bayi"
    elif age < 4:
        stage = "balita"
    elif age < 13:
        stage = "anak-anak"
    elif age < 20:
        stage = "remaja"
    elif age < 65:
        stage = "dewasa"
    else:
        stage = "lansia"
    print(f"Umur {age} tahun: {stage}")