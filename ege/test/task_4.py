"""
(Е. Джобс) Исполнитель Редактор получает на вход строку цифр и преолбразовывает её. Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки символов.
    заменить (v, w)
    нашлось (v)
Первая команда заменяет в строке первое слева вхожденгие цепочки v на цепочку w. Если цепочки v в строке нет, эта команда не изменяет строку. Вторая команда проверяет, встречается ли цепочка v в строке испольнителя Редактор.

Дана программа для Редактора:
    ПОКА нашлось (11)
        заменить (112, 4)
        заменить (113, 2)
        заменить (42, 3)
        заменить (43, 1)
    КОНЕЦ ПОКА

Какая строка получится в результате применения приведённой про граммы к строке вида 1...13..32...2, состоящей из 170 единиц, 100 троек и 7 двоек?
"""


string = "1" * 170 + "3" * 100 + "2" * 7
while "11" in string:
    string = string.replace("112", "4", 1)
    string = string.replace("113", "2", 1)
    string = string.replace("42", "3", 1)
    string = string.replace("43", "1", 1)

print(string)