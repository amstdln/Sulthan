def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(f"Mengirim pesan: {message}")
        sent_messages.append(message)

messages = [
    "Selamat pagi!",
    "Semangat belajar!",
    "Jangan lupa mengerjakan tugas."
]

sent_messages = []

send_messages(messages, sent_messages)

print("\nDaftar pesan tersisa:")
print(messages)

print("\nPesan yang sudah dikirim:")
print(sent_messages)