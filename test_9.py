"""Генерация целых чисел"""

from timeit import default_timer, timeit


def gen_prime(x):
    multiples = []
    results = []
    for i in range(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in range(i*i, x+1, i):
                multiples.append(j)

    return results


# левая отсечка времени
start_time = default_timer()
# запуск функции
gen_prime(3000)
# правая отсечка времени и результат
print(default_timer() - start_time)

# сравним с привычным вариантом замеров
print(timeit("gen_prime(3000)", setup="from __main__ import gen_prime", number=1))

"""
0.0578244
0.05766979999999999

Существенных расхождений не выявлено
"""