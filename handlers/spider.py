from datetime import datetime
from typing import List, Union

import pytz
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from core.browser import Browser
from core.date_time import current_time, get_sleep


class Spider:
    def __init__(self, url_start: str):
        self.driver: Browser = Browser()
        self.datetime_start = datetime.now(pytz.timezone("Asia/Novosibirsk"))
        self.url_start = url_start

    def open_browser(self) -> None:
        """
        Открываем браузер.
        """
        browser_instance = Browser()
        self.driver = browser_instance

    def exit_browser(self) -> None:
        """
        Выходим из браузера.
        """
        if self.driver:
            self.driver.quit()

    def goto_url(self, url: str) -> None:
        """
        Переходим по url.
        """
        print(f"url => {url}")
        self.driver.get(url)

    def run(self):

        try:
            self.goto_url(self.url_start)

            get_sleep(2, 4)

            self.driver.scroll_to_bottom_of_page(True)

            get_sleep(20, 20)

            self.exit_browser()

        except KeyboardInterrupt:
            self.exit_browser()
