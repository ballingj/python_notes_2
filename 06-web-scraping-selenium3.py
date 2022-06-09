# Python program to demonstrate selenium
# using find_element
# https://itsmycode.com/find-element-by-commands-are-deprecated/
# 


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


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
  driver.get("https://itsmycode.com/find-element-by-commands-are-deprecated/")
  return driver


def main():
  driver = get_driver()
  # get element
  element = driver.find_element(By.ID, "post-3734")
  driver.quit()   #closes the browser
  # return complete
  return element


print(main())

