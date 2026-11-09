
text = input("Soz ve ya cumle daxil edin: ")

vowels = "aeeıioöuüə"
count = 0

for letter in text:
    if letter.lower() in vowels:
        count = count + 1

print("Saitlerin sayi:", count)
