rivers = {
    "Nil": "Mesir",
    "Amazon": "Amerika Selatan",
    "Kapuas": "Indonesia"
}

for river, country in rivers.items():
    print(f"Sungai {river} berada di {country}.")

print("\nNama sungai:")
for river in rivers:
    print(river)

print("\nNegara atau wilayah:")
for country in rivers.values():
    print(country)