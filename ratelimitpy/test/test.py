from ratelimitpy.core import ratelimitpy


# Should print no more than 10 calls for every 2 second period
@ratelimitpy(calls=10, period=2)
def fib(n):
    print(n)
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(6))
