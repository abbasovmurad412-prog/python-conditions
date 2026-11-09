
temperatures = [-3, 2, 8, 15, 22, 27, 31]

for i in range(len(temperatures)):

    temp = temperatures[i]

    if temp < 0:
        weather = "Shaxta"

    elif temp <= 9:
        weather = "Soyuq"

    elif temp <= 19:
        weather = "Mülayim"

    elif temp <= 29:
        weather = "Isti"

    else:
        weather = "Cox isti"

    print(i + 1, "-ci gun:", temp, "->", weather)
