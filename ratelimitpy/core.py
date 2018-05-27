from functools import wraps
import threading


class ratelimitpy:
    """
    Simple rate limit decorator class
    """

    def __init__(self, calls, period):
        """
        :param calls: int, greater than 0, the maximum number of calls to execute during the time 'period'
        :param period: int or float, greater than 0, time in seconds during which a maximum of x number of
            'calls' can be executed
        """
        self.calls = calls
        self.period = period
        self.semaphore = threading.Semaphore(self.calls)

    def __call__(self, func):
        """
        :param func: The function being decorated
        :return: wrapper, the wrapper function that will get used by the decorator
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                self.semaphore.acquire()
                return func(*args, **kwargs)
            finally:
                t = threading.Timer(interval=self.period, function=self.semaphore.release)
                t.setDaemon(True)
                t.start()
        return wrapper
