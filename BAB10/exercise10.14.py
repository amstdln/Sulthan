from pathlib import Path
import json


def get_new_username():
    username = input("Masukkan nama pengguna baru: ")

    path = Path("username.json")
    contents = json.dumps(username)
    path.write_text(contents)

    return username


def greet_user():
    path = Path("username.json")

    if path.exists():
        username = json.loads(path.read_text())

        print(f"Apakah nama pengguna Anda {username}?")
        answer = input("Masukkan y atau n: ")

        if answer.lower() == "y":
            print(f"Selamat datang kembali, {username}!")

        else:
            username = get_new_username()
            print(f"Nama pengguna berhasil diperbarui. Selamat datang, {username}!")

    else:
        username = get_new_username()
        print(f"Kami akan mengingat Anda saat kembali, {username}!")


greet_user()