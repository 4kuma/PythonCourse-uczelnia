from random import randrange
import time


def count_function_time(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        print(f'Time: {time.time() - start}')

    return wrapper


@count_function_time
def generate_random_numbers(count):
    for _ in range(count):
        randrange(1, 10000)


if __name__ == '__main__':
    generate_random_numbers(10000)
