import math

number = int(input())

"""
    Тут мне стало очень скучно и я решил использовать формулу Бине ... 😒😒😒
"""

phi = (1 + math.sqrt(5)) / 2
fib = (phi ** number / math.sqrt(5) + 0.5)
print(int(fib))