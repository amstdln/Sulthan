prompt = "Masukkan nama kamu (ketik 'quit' untuk berhenti): "

while True:
    name = input(prompt)

    if name == "quit":
        break

    print(f"Halo, {name}!")