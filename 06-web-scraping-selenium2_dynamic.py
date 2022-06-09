"""
Part 2 - scraping dynamic contents
Now we are after an element that dynamically changes.  We need to use the time module to freeze or sleep to capture the contents
"""
"""
prerequisite:
need to install selenium
need to install chrome driver
need to follow this directions if using wsl:  https://www.gregbrisebois.com/posts/chromedriver-in-wsl2/
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time   # import time to use sleep function

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
  driver.get("http://automated.pythonanywhere.com")
  return driver

def clean_text(text, driver):
  """Extract only the temperature from test"""
  output = float(text.split(": ")[1])
  driver.quit()
  return output

def main():
  driver = get_driver()
  time.sleep(2)   # sleep for two seconds
  element = driver.find_element(
      by="xpath", value="/html/body/div[1]/div/h1[2]")
  # driver.quit()  # closes the browser
  return clean_text(element.text, driver)


print(main())
