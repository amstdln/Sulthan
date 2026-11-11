class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]

    def show_privileges(self):
        print("Hak akses administrator:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Membuat objek administrator
admin = Admin("Andi", "Saputra")

admin.show_privileges()