cities = {
    "Surakarta": {
        "country": "Indonesia",
        "population": 500000,
        "fact": "Dikenal sebagai Kota Solo."
    },
    "Tokyo": {
        "country": "Jepang",
        "population": 14000000,
        "fact": "Merupakan ibu kota Jepang."
    },
    "Paris": {
        "country": "Prancis",
        "population": 2100000,
        "fact": "Terkenal dengan Menara Eiffel."
    }
}

for city, information in cities.items():
    print(f"\nKota: {city}")
    for key, value in information.items():
        print(f"{key}: {value}")