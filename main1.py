from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import json

cookies = []

with open("cookies.json", 'r') as cookieString:
    cookies = json.load(cookieString)

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--remote-debugging-port=9222')
options.binary_location = '/usr/bin/chromium-browser'
driver = webdriver.Chrome(options = options)

driver.get("https://bilibili.com")

for cookie in cookies:
    driver.add_cookie(cookie)

driver.get("https://www.bilibili.com/video/BV1b44y1q7Cb")

time.sleep(1)
driver.get_screenshot_as_file('test.png')


ActionChains(driver).move_by_offset(400, 400).click().perform()

time.sleep(1)

driver.get_screenshot_as_file('test1.png')

for i in range(10):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(1)

driver.get_screenshot_as_file('test2.png')

comments = driver.execute_script("return document.querySelector('#commentapp > bili-comments').shadowRoot.querySelectorAll('#feed > bili-comment-thread-renderer').length")
print(comments)