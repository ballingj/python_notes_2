"""
prerequisite:
need to install selenium
need to install chrome driver
need to follow this directions if using wsl:  https://www.gregbrisebois.com/posts/chromedriver-in-wsl2/
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# service = Service('C:\\Users\\Jeff\\Downloads\\chromedriver.exe') # windows
service = Service('/usr/bin/chromedriver')  # wsl2


def get_driver():
  # Set options to allow browser scraping
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximize")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(service=service, options=options)
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver


def main():
  driver = get_driver()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  print(driver.current_url)

print(main())
