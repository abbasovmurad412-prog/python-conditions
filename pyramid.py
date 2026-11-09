
rows = int(input("Setir sayini daxil edin: "))

if rows < 0:
    print("Xeta: Menfi eded olmaz")

else:
    for i in range(1, rows + 1):
        print("*" * i)