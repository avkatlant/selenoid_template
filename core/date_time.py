import time
import random
import pytz
import datetime

from typing import Union


def sleep(arg1, arg2):
    t = random.uniform(arg1, arg2)

    def outer(func):
        def wrapper(*args, **kwargs):

            result = func(*args, **kwargs)

            print(f"decorator sleep({arg1}, {arg2}) => {t}")
            time.sleep(t)

            return result
        return wrapper
    return outer


def get_sleep(arg1: Union[int, float], arg2: Union[int, float]) -> float:
    t = random.uniform(arg1, arg2)
    # print(f"func get_sleep({arg1=}, {arg2=}) => {t}")
    time.sleep(t)
    return t


def current_time():
    timezone = pytz.timezone("Asia/Novosibirsk")
    now_with_tz = timezone.localize(datetime.datetime.now())
    return now_with_tz
