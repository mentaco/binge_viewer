import sys
import getpass
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

class BingeViewer:
    def __init__(self, url):
        self.start_url = url
        self.service = Service(executable_path=GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=self.service)
        self.wait = WebDriverWait(driver=self.driver, timeout=15)
    
    def start_viewing(self):
        self.driver.get(self.start_url)

        if self.login():
            self.driver.quit()

        self.video_view()
        self.next_video()

    def login(self):
        self.wait.until(EC.presence_of_all_elements_located)

        while True:
            try:
                userid = self.driver.find_element(By.ID, "login-username")
                password = self.driver.find_element(By.ID, "login-password")

                userid.send_keys(input("your id > "))
                password.send_keys(getpass.getpass("your password > "))

                login_button = self.driver.find_element(By.ID, "btn-login")
                login_button.click()

                self.wait.until(EC.presence_of_all_elements_located)

                if "ログインに失敗" in self.driver.page_source:
                    print("Login failed.")
                    
                elif "指定回数を超えた" in self.driver.page_source:
                    print("Authentication locked.")
                    return 1
                else:
                    print("Login success.")
                    return 0
            except Exception as e:
                print(e)
                print("An error has occurred.")
                return 1

    def video_view(self):
        play_btn = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "vjs-big-play-button")))
        play_btn.click()
    
    def next_video(self):
        video_title = self.driver.find_element(By.XPATH, "//section[@id='region-main']/div/h2")
        print(f"Start viewing \"{video_title.text}\"")

        while True:
            remaining_t = self.driver.find_element(By.CLASS_NAME, "vjs-remaining-time-display")
            if remaining_t.text == "0:00":
                break
            sleep(15)
        print(f"Finish viewing \"{video_title.text}\"")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <URL>")
        print("URLs should be enclosed in single or double quotation marks.")
    else:
        viewer = BingeViewer(sys.argv[1])
        viewer.start_viewing()
