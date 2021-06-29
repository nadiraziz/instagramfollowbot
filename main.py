from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException


CHROMEDRIVER_PATH = "C:\Development\chromedriver.exe"
USERNAME = 'mobile__kart'
PASSWORD = 'fadhil@123'
SIMILAR_ACCOUNT = 'hananshaah'

URL = 'https://www.instagram.com'


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROMEDRIVER_PATH)

    def login(self):
        self.driver.get(f'{URL}/accounts/login/')
        time.sleep(3)
        username_input = self.driver.find_element_by_name('username')
        username_input.send_keys(USERNAME)
        pass_input = self.driver.find_element_by_name('password')
        pass_input.send_keys(PASSWORD)
        pass_input.send_keys(Keys.ENTER)

        time.sleep(3)

        save_or_not = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
        save_or_not.click()

        time.sleep(6)

        notification = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notification.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div')
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

check = InstaFollower()
check.login()
check.find_followers()
check.follow()