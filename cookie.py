from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

timeout = time.time() + 60 * 5  # 5 minutes from now

driver = webdriver.Chrome()

driver.get("http://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

cookie = driver.find_element(By.ID, "cookie")
required_money = None
ID_list = ["buyTime\ machine", "buyPortal",
           "buyAlchemy\ lab", "buyShipment", "buyMine", "buyFactory",
           "buyGrandma", "buyCursor"]
while time.time() < timeout:
    checker = time.time() + 10
    while time.time() < checker:
        cookie.click()
    for ids in ID_list:
        something = driver.find_element(by=By.CSS_SELECTOR, value=f"#{ids} > b")
        try:
            required_money = locale.atof(something.text.split("-")[1])
        except:
            pass
        money = locale.atof(driver.find_element(by=By.ID, value="money").text)

        if (required_money < money) or (required_money == money):
            time.sleep(1)
            driver.find_element(by=By.ID, value=ids).click()
time.sleep(1)
print(driver.find_element(by=By.ID, value="cps").text)
