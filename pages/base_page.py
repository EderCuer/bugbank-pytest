from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import BASE_URL, TIMEOUT

class BasePage:
  def __init__(self, driver, path=""):
    self.driver = driver
    self.url = BASE_URL + path

  def set_local_storage(self, key, value):
    """Define um item no local storage."""
    self.driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")

  def open(self):
    self.driver.get(self.url)

  def find_element(self, by, value, timeout=TIMEOUT):
    try:
      element = WebDriverWait(self.driver, timeout).until(
        EC.visibility_of_element_located((by, value))
      )
      return element
    except TimeoutException:
      print(f"Element not found: {value}")
    return None

  def click(self, by, value, timeout=TIMEOUT):
    element = self.find_element(by, value, timeout)
    if element:
      element.click()

  def enter_text(self, by, value, text, timeout=TIMEOUT):
    element = self.find_element(by, value, timeout)
    if element:
      element.clear()
      element.send_keys(text)