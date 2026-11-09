
experience = float(input("Təcrübə illərini daxil edin: "))
score = float(input("Müsahibə balını daxil edin (0-100): "))

if experience < 0 or score < 0 or score > 100:
    print("Xəta: Yanlış məlumat daxil edildi!")

elif score >= 90:
    print("Güclü namizəd")

elif experience >= 2 and score >= 70:
    print("Növbəti mərhələyə dəvət olunur")

else:
    print("Namizəd uyğun deyil")

status = "İlkin mərhələni keçdi" if score >= 90 or (experience >= 2 and score >= 70) else "İlkin mərhələni keçmədi"

if experience >= 0 and 0 <= score <= 100:
    print(status)
