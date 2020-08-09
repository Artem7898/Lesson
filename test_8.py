from time import sleep
from timeit import repeat, default_timer


class TestClass:

    @staticmethod
    def some_slow_method(loop_count):
        for i in range(loop_count):
            sleep(1)

    @staticmethod
    def some_quick_method(loop_count):
        for i in range(loop_count):
            sleep(0.1)


if __name__=='__main__':
    # Для того что бы воспользоваться классом необходимого модуля,
    # его необходимо импортировать в инициализирующем выражении setup
    # а также создать экземпляр класса

    setup = """
from __main__ import TestClass
test = TestClass()
    """
    statements = ['test.some_slow_method(5)',
                  'test.some_slow_method(3)',
                  'test.some_quick_method(5)',
                  'test.some_quick_method(3)']

    for st in statements:
        print(f'{st}, {min(repeat(st, setup, default_timer, 3, 1))}')

"""
test.some_slow_method(5), 5.002561600000001
test.some_slow_method(3), 3.000246899999997
test.some_quick_method(5), 0.5015900000000002
test.some_quick_method(3), 0.30135129999999677
"""