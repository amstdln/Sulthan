from pathlib import Path

path = Path("Prokom1/Scripts/exercise10/learning_python.txt")

contents = path.read_text()

for line in contents.splitlines():
    new_line = line.replace("Python", "C")
    print(new_line)