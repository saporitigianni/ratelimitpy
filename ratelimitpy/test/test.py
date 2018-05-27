from ratelimitpy.core import ratelimitpy


# Should print no more than 10 call for every 3 second period
@ratelimitpy(calls=10, period=3)
def print_limited(data):
    print(data)


if __name__ == '__main__':
    for x in range(30):
        print_limited(x)
