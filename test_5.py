"""Профилировка"""

import cProfile


def get_count(items):
    return items.__len__()


def get_sum(items):
    sum = 0
    for i in items:
        sum += i
    return sum


def main():
    my_lst = [3, 5, 6, 7]
    res_count = get_count(my_lst)
    res_sum = get_sum(my_lst)


cProfile.run('main()')