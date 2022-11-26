import time
from datetime import timedelta

from handlers.spider import Spider


def main():
    start_time = time.monotonic()

    url = "https://21-school.ru/"

    dc = Spider(url_start=url)
    dc.run()

    time_work = time.monotonic() - start_time
    print(f"\nTIME: {time_work} / {timedelta(seconds=time_work)}")


if __name__ == "__main__":
    main()
