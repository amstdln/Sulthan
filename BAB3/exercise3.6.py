guests = ["Budi", "Dina", "Citra"]

print("Saya menemukan meja makan yang lebih besar.")

guests.insert(0, "Andi")
guests.insert(2, "Rudi")
guests.append("Sinta")

for guest in guests:
    print(f"Halo {guest}, kamu diundang makan malam.")