"""from random import randint
numlist=[1,2,3,4,5,6,7,8,9]
num=0
n=0
while n<=3:
    rn=randint(1, 8-n)
    num+=numlist[rn]*(10**n)
    numlist.remove(rn-1)
    n+=1
print(num)"""

import random

def generate_random_number():
    # Создаем список цифр от 0 до 9
    digits = list(range(10))

    # Перемешиваем список цифр случайным образом
    random.shuffle(digits)

    # Выбираем первые четыре цифры из перемешанного списка и объединяем их в число
    random_number = int(''.join(map(str, digits[:4])))

    return random_number

# Пример использования
random_number = generate_random_number()
print(random_number)