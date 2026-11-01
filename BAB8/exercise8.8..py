def make_album(artist, title, songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if songs is not None:
        album["songs"] = songs

    return album

while True:
    print("\nMasukkan informasi album.")
    print("Ketik 'q' untuk berhenti.")

    artist = input("Nama penyanyi: ")
    if artist.lower() == "q":
        break

    title = input("Judul album: ")
    if title.lower() == "q":
        break

    print(make_album(artist, title))