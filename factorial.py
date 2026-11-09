
number = int(input("Bir eded daxil edin: "))

factorial = 1

if number < 0:
    print("Menfi ededin faktoriali yoxdur")

else:
    for i in range(1, number + 1):
        factorial = factorial * i

    print("Faktorial:", factorial)
