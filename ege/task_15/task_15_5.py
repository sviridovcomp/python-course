"""
На числовой прямой даны отрезки A = [70; 90], B = [40; 60] и C = [0; N] и функция
            F(x) = (¬(x ∈ A) -> (x ∈ B)) && (¬(x ∈ C) -> (x ∈ A) )
При каком наименьшем числе N функция F(x) истинна более чем для 30 целых чисел x?
"""

P = {i for i in range(70, 91)}
B = {i for i in range(40, 61)}
C = set()

for i in range(100):
    C.add(i)
    if (len(A) + len(B & C)) > 30:
        print(i)
        break