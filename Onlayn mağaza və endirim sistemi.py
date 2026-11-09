
amount = float(input("Sifarişin məbləğini daxil edin: "))

if amount < 0:
    print("Xəta: Məbləğ mənfi ola bilməz!")

elif amount >= 200:
    discount = amount * 0.20
    total = amount - discount
    print("Endirim: 20%")
    print("Yekun məbləğ:", total)

elif amount >= 100:
    discount = amount * 0.10
    total = amount - discount
    print("Endirim: 10%")
    print("Yekun məbləğ:", total)

else:
    total = amount
    print("Endirim yoxdur")
    print("Yekun məbləğ:", total)

status = "Endirim qazandınız" if amount >= 100 else "Endirim yoxdur"

if amount >= 0:
    print(status)
