guests = ["Andi", "Budi", "Citra", "Dina", "Rudi", "Sinta"]

print("Maaf, saya hanya bisa mengundang dua orang.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Maaf {removed_guest}, kamu tidak bisa diundang.")

for guest in guests:
    print(f"{guest}, kamu tetap diundang.")

del guests[0]
del guests[0]

print(guests)