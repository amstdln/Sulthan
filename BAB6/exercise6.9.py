favorite_places = {
    "Andi": ["Bali", "Yogyakarta"],
    "Budi": ["Bandung"],
    "Citra": ["Jepang", "Swiss", "Korea Selatan"]
}

for name, places in favorite_places.items():
    print(f"Tempat favorit {name}:")
    for place in places:
        print(f"- {place}")