while True:
    age = int(input("Укажите год рождения А.С.Пушкина: "))
    if age == 1799:
        break
    else:
        print('Не верный год рождения')
while True:
    day = str(input("Укажите день рождения А.С.Пушкина (день.месяц): "))
    if day == "06.06":
        break
    else:
        print('Не верная дата рождения')
print("Отлично!")


