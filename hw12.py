#!/usr/bin/env python3
def fib(n):
    fib1=fib2=1
    if n<=0:
        raise ValueError
    elif n in (1, 2):
        return 1
    n = int(n) - 2
    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    return fib2


if __name__ == "__main__":
    print(fib(5432))
