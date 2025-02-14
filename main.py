import random
import json

with open("bd.json", encoding="utf-8") as file:
    json_lst = json.load(file)
    print(json_lst)
correct_ans = 0
incorrect_ans = 0
answers = {0: "слитно", 1: "раздельно"}

while True:
    # 1 - раздельно 0 - слитно
    try:
        n = random.randint(0, 1)
        n_word = random.randint(0, len(json_lst[n][str(n)])-1)
        user_ans = int(input(f"{json_lst[n][str(n)][n_word]} 0 - слитно, 1 - раздельно, 5 - завершить игру\n"))
        if user_ans == 5:
            stat = (correct_ans / (correct_ans + incorrect_ans) * 100)
            print(f"Вы правильно решили {stat}% заданий")
            break
        elif user_ans == n:
            correct_ans += 1
            print("Верно!")
        else:
            incorrect_ans += 1
            total_ans = answers[n]
            print(f"Неверно! Это слово пишется {total_ans}")
    except ValueError as e:
        print("Введите только 0/1/5")