def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    totalsequence = []
    for index, val in enumerate(fib(300)):
        totalsequence.append(val)
        print(totalsequence[index]/totalsequence[index-1])

from math import sqrt


if __name__ == '__main__':
    main()
