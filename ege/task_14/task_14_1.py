"""
(С.С Поляков, Саратов) Значение выражения 7 * 6561^46 + 8 * 729^15 - 6 * 5832 записали в системе счисления с основанием 9. Сколько цифр 7 содержится в этой записи?
"""


expr = 7 * 6561 ** 46 + 8 * 729 ** 15 - 6 * 5832
result = ""
while expr:
    result += str(expr % 9)
    expr //= 9

print(result.count("7"))