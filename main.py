import sys
import getpass
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def login(driver):
    userid = driver.find_element(By.ID, "login-username")
    password = driver.find_element(By.ID, "login-password")

    _id = input("your id > ")
    _passwd = getpass.getpass("your password > ")
    userid.send_keys(_id)
    password.send_keys(_passwd)

    login_button = driver.find_element(By.ID, "btn-login")
    login_button.click()

def video_view(url):
    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get(url)

    login(driver)

    sleep(3)
    driver.quit()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <URL>")
        print("URLs should be enclosed in single or double quotation marks.")
    else:
        video_view(sys.argv[1])
