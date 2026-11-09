
scores = [78, 92, 65, 88, 100, 54, 91, 73]

total = 0
count = 0
highest = scores[0]

for score in scores:
    total = total + score

    if score >= 90:
        count = count + 1

    if score > highest:
        highest = score

average = total / len(scores)

print("Ballarin cemi:", total)
print("Orta bal:", average)
print("90 ve yuxari bal alanlar:", count)
print("En yuksek bal:", highest)
