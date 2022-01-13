from random import shuffle, randint
from time import time


def get_timing(func: callable):
    def inner():
        start_time = time()
        func()
        print(f"{func} elapsed time: {time() - start_time} s")
    return inner


@get_timing
def traditional_random():
    for _ in range(10000):
        print(randint(1, 1000))


@get_timing
def doom_random():
    intlist = [x for x in range(1000)]
    shuffle(intlist)
    for _ in range(10000):
        print(randint(1, 1000))


def main():
    traditional_random()
    doom_random()


if __name__ == "__main__":
    main()
