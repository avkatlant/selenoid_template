import random
import datetime
from typing import List, Union
from typing_extensions import Self

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from core.date_time import get_sleep


class Browser(webdriver.Remote):

    def __init__(self):
        command_executor = 'http://localhost:4444/wd/hub'

        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("start-maximized")
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')

        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationControlled")

        # date_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        # self.name_resource = name_resource
        # capabilities = {
        #     "browserName": "chrome",
        #     "name": f"{date_time} -- {self.name_resource}",
        #     "version": "80.0",
        #     "platform": "LINUX",
        #     "enableVNC": True
        #     # "enableLog": True,
        #     # "logName": f"{date_time}__{self.name_resource}.log"
        # }

        date_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "80.0",
            "selenoid:options": {
                "name": f"{date_time}",
                "enableVNC": True,
                "enableVideo": False
            }
        }

        super().__init__(
            command_executor=command_executor,
            desired_capabilities=capabilities, options=options)

        self.__wait = WebDriverWait(self, 5, 0.3)

        self.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def __get_selenium_by(self, find_by: str):
        """Return a dictionary, where Keys are Strings representing a search locator
        strategies and Values are related By class values.
        """
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'class_name': By.CLASS_NAME,
                    'id': By.ID,
                    'link_text': By.LINK_TEXT,
                    'name': By.NAME,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'tag_name': By.TAG_NAME}
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = "") -> WebElement:
        """Waiting on element and return WebElement if it is visible.
        """
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = "") -> WebElement:
        """Waiting on element and return WebElement if it is present on DOM.
        """
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = "") -> WebElement:
        """Wait on element until it disappears (Ждем пока элемент не пропадет со страницы).
        """
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def is_staleness_of(self, find_by: str, locator: str, locator_name: str = "") -> WebElement:
        """Wait on element until it disappears (Ждем пока элемент не пропадет со страницы).
        """
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = "") -> List[WebElement]:
        """Waiting on elements and return WebElements if they are visible.
        """
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = "") -> List[WebElement]:
        """Waiting on elements and return WebElements if they are present on DOM.
        """
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def get_text_from_webelements(self, elements: List[WebElement]) -> List[str]:
        """The input should be a list of WebElements, where we read text from each element and Return a List[String].
        """
        return [element.text for element in elements]

    def get_element_by_text(self, elements: List[WebElement], name: str) -> WebElement:
        """The input should we a list of WebElements, from which we return a single WebElement found by it's name.
        """
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

    def delete_cookie_by_name(self, cookie_name: str) -> None:
        """Delete a cookie by a name.
        """
        self.delete_cookie(cookie_name)

    def scroll_to_bottom_of_page(self, go_back_to_top: bool = False):
        """Scrolling to the end of the page.
        """
        page_height = self.execute_script(
            "return document.body.scrollHeight")  # Get scroll height

        n = random.randint(5, 10)
        get_one_scroll = page_height / n

        for i in range(1, n + 1):
            # Scroll down to bottom
            self.execute_script(
                f"window.scrollTo(0, {get_one_scroll * i});")

            # Wait to load page
            get_sleep(0.1, 0.7)

        if go_back_to_top:
            self.execute_script("window.scrollTo(0, 0);")

    def close_tab_browser(self):
        """Close the browser Tab.
        """
        self.close()
        self.switch_to.window(
            self.window_handles[-1])
