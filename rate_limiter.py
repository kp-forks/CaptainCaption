import threading
import time


class RateLimiter:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = 0
        self.lock = threading.Lock()

    def reset(self):
        with self.lock:
            self.calls = 0

    def add_call(self):
        with self.lock:
            self.calls += 1

    def wait(self):
        while True:
            with self.lock:
                if self.calls < self.max_calls:
                    break
            time.sleep(1)


def reset_limiter_periodically(limiter, period):
    while True:
        time.sleep(period)
        limiter.reset()
