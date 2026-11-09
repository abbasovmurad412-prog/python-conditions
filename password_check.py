
password = input("Shifreni daxil edin: ")

upper = 0
lower = 0
digits = 0
other = 0

for char in password:

    if char.isupper():
        upper = upper + 1

    elif char.islower():
        lower = lower + 1

    elif char.isdigit():
        digits = digits + 1

    else:
        other = other + 1

print("Boyuk herf:", upper)
print("Kicik herf:", lower)
print("Reqem:", digits)
print("Diger simvol:", other)

if len(password) > 8 and upper > 0 and lower > 0 and digits > 0 and other > 0:
    print("Shifre gucludur")

else:
    print("Shifre guclu deyil")
