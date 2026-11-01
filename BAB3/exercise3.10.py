motorcycles = ["Honda", "Yamaha", "Suzuki", "Kawasaki"]

# Mengakses elemen
print(motorcycles[0])

# Mengubah elemen
motorcycles[0] = "Ducati"

# Menambahkan elemen
motorcycles.append("BMW")

# Menambahkan elemen pada posisi tertentu
motorcycles.insert(1, "Vespa")

# Menghapus elemen
del motorcycles[2]

# Menghapus menggunakan pop
motorcycles.pop()

# Mengurutkan daftar
motorcycles.sort()

# Mengurutkan sementara
print(sorted(motorcycles))

# Membalik urutan
motorcycles.reverse()

# Menghitung jumlah elemen
print(len(motorcycles))

print(motorcycles)