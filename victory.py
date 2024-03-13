correct_answer = 0
incorrect_answer = 0
all_question = 5
while True:
    correct_answer = 0
    incorrect_answer = 0
    pushkin = int(input("Укажите год рождения Пушкина: "))
    if pushkin == 1799:
        print("Правильно!")
        correct_answer += 1
    else:
        print("Неправильно! Правильный год рождения: 1799")
        incorrect_answer += 1
    abai = int(input("Укажите год рождения Абая: "))
    if abai == 1845:
        print("Правильно!")
        correct_answer += 1
    else:
        print("Неправильно! Правильный год рождения: 1845")
        incorrect_answer += 1
    lermontov = int(input("Укажите год рождения Лермонтова: "))
    if lermontov == 1814:
        print("Правильно!")
        correct_answer += 1
    else:
        print("Неправильно! Правильный год рождения: 1814")
        incorrect_answer += 1
    tolstoi = int(input("Укажите год рождения Толстого: "))
    if tolstoi == 1828:
        print("Правильно!")
        correct_answer += 1
    else:
        print("Неправильно! Правильный год рождения: 1828")
        incorrect_answer += 1
    auezov = int(input("Укажите год рождения Ауэзова: "))
    if auezov == 1897:
        print("Правильно!")
        correct_answer += 1
    else:
        print("Неправильно! Правильный год рождения: 1897")
        incorrect_answer += 1
    print("\nРезультаты:")
    print("Правильные ответы:", correct_answer)
    print("Ошибки:", incorrect_answer)
    #all_question = len(famous_person)
    print("Процент правильных ответов:", (correct_answer * 100) / all_question, "%")
    print("Процент неправильных ответов:", (incorrect_answer * 100) / all_question, "%")
    test = str(input("Хотите начать с начала? (да/нет) "))
    if test.lower() == "нет":
        print("Спасибо за игру!")
        break




