"""Профилировка времени выполнения функций"""

import cProfile
import time


def fast():
    print("Я быстрая функция")


def slow():
    time.sleep(3)
    print("Я очень медленная функция")


def medium():
    time.sleep(0.5)
    print("Я средняя функция...")


def main():
    fast()
    slow()
    medium()


cProfile.run('main()')