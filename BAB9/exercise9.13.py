from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


# Dadu 6 sisi
die1 = Die()

print("Dadu 6 sisi:")
for i in range(10):
    die1.roll_die()


# Dadu 10 sisi
die2 = Die(10)

print("Dadu 10 sisi:")
for i in range(10):
    die2.roll_die()


# Dadu 20 sisi
die3 = Die(20)

print("Dadu 20 sisi:")
for i in range(10):
    die3.roll_die()