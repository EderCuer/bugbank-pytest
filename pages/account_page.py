from selenium.webdriver.common.by import By
from .base_page import BasePage

class AccountPage(BasePage):
  # Localizadores
  TEXT_NAME = (By.ID, 'textName')

  def get_welcome_message(self):
    message_element = self.find_element(*self.TEXT_NAME)
    return message_element.text.strip() if message_element else ""