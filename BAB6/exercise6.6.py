favorite_languages = {
    "Andi": "Python",
    "Budi": "Java",
    "Citra": "Python",
    "Doni": "C++"
}

people = ["Andi", "Budi", "Eko", "Citra", "Fajar"]

for person in people:
    if person in favorite_languages:
        print(f"Terima kasih, {person}, sudah mengikuti polling.")
    else:
        print(f"{person}, silakan mengikuti polling bahasa pemrograman favorit.")