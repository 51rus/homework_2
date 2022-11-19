# запускаем счетчик
counter = 0

# приветствие, знакомство и начало теста
print("Привет! Предлагаю проверить свои знания английского!")
print("Расскажи, как тебя зовут!")
user_test_name = input()
print(f"Привет, {user_test_name}, начинаем тренировку!")

# первый вопрос теста
print("My name ___ Vova")
user_answer_1 = input()
# условие и вывод верного ответа
if user_answer_1 == "is":
    counter += 1
    print("Ответ верный!")
    print("Вы получаете 10 баллов!")
# если ответ неверный
else:
    print("Неправильно.")
    print("Правильный ответ: is")

# второй вопрос теста
print("I ___ a coder")
user_answer_2 = input()
# условие и вывод верного ответа
if user_answer_2 == "am":
    counter += 1
    print("Ответ верный!")
    print("Вы получаете 10 баллов!")
# если ответ неверный
else:
    print("Неправильно.")
    print("Правильный ответ: am")

# третий вопрос теста
print("I live ___ Moscow")
user_answer_3 = input()
# условие и вывод верного ответа
if user_answer_3 == "in":
    counter += 1
    print("Ответ верный!")
    print("Вы получаете 10 баллов!")
# если ответ неверный
else:
    print("Неправильно.")
    print("Правильный ответ: in")

# вычисление результатов теста
score = counter * 10
# добавлю round для округления, иначе много знаков после запятой
score_percent = round(counter / 3 * 100)

# завершение теста
print(f"Вот и все, {user_test_name}!")
print(f"Вы ответили на {counter} вопросов из 3 верно.")
print(f"Вы заработали {score} баллов.")
print(f"Это {score_percent} процентов.")