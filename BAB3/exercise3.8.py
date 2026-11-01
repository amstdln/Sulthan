places = ["Jepang", "Swiss", "Korea Selatan", "Turki", "Australia"]

print("Daftar asli:")
print(places)

print("\nUrutan alfabet:")
print(sorted(places))

print("\nDaftar asli kembali:")
print(places)

print("\nUrutan alfabet terbalik:")
print(sorted(places, reverse=True))

print("\nDaftar asli kembali:")
print(places)

places.reverse()
print("\nSetelah reverse:")
print(places)

places.reverse()
print("\nKembali ke urutan awal:")
print(places)

places.sort()
print("\nSetelah sort:")
print(places)

places.sort(reverse=True)
print("\nUrutan terbalik:")
print(places)