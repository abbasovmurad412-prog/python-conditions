
students = [
    ("Aysel", 95),
    ("Murad", 72),
    ("Leyla", 84),
    ("Elvin", 48),
    ("Nigar", 63)
]

for name, score in students:

    if score >= 91:
        grade = "A"

    elif score >= 81:
        grade = "B"

    elif score >= 71:
        grade = "C"

    elif score >= 61:
        grade = "D"

    elif score >= 51:
        grade = "E"

    else:
        grade = "F"

    print(name + ":", score, "->", grade)
