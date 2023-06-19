import sys
import getpass
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def login(driver, wait):
    while True:
        try:
            userid = driver.find_element(By.ID, "login-username")
            password = driver.find_element(By.ID, "login-password")

            _id = input("your id > ")
            _passwd = getpass.getpass("your password > ")
            userid.send_keys(_id)
            password.send_keys(_passwd)

            login_button = driver.find_element(By.ID, "btn-login")
            login_button.click()

            wait.until(EC.presence_of_all_elements_located)

            if "ログインに失敗" in driver.page_source:
                print("Login failed.")
                
            elif "指定回数を超えた" in driver.page_source:
                print("Authentication locked.")
                return 1
            else:
                print("Login success.")
                return 0
        except Exception as e:
            print(e)
            print("An error has occurred.")
            return 1

def video_view(url):
    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    wait = WebDriverWait(driver=driver, timeout=15)

    driver.get(url)

    if login(driver, wait):
        driver.quit()

    play_btn = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "vjs-big-play-button")))
    play_btn.click()
    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <URL>")
        print("URLs should be enclosed in single or double quotation marks.")
    else:
        video_view(sys.argv[1])
