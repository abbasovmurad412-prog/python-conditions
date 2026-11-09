
income = float(input("Aylıq gəliri daxil edin: "))
expenses = float(input("Ümumi xərcləri daxil edin: "))

if income < 0 or expenses < 0:
    print("Xəta: Mənfi məbləğ daxil etmək olmaz!")

elif income == 0:
    if expenses > 0:
        print("Büdcə kəsiri var")
    else:
        print("Gəlir və xərc sıfırdır")

else:
    remaining = income - expenses
    saving = (remaining / income) * 100

    if expenses > income:
        print("Büdcə kəsiri var")

    elif expenses >= income * 0.80:
        print("Xərclərə diqqət et")

    elif expenses >= income * 0.50:
        print("Büdcə normaldır")

    else:
        print("Yaxşı qənaət edirsiniz")

    print("Qalan pul:", remaining, "AZN")
    print("Qənaət faizi:", saving, "%")
