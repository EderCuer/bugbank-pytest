import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .login_page import LoginPage

class RegisterPage(BasePage):

  # Localizadores
  EMAIL_INPUT = (By.XPATH, '(//input[@name="email"])[2]')
  NAME_INPUT = (By.NAME, 'name')
  PASSWORD_INPUT = (By.XPATH, '(//input[@name="password"])[2]')
  PASSWORD_CONFIRMATION_INPUT = (By.NAME, 'passwordConfirmation')
  TOGGLE_BALANCE = (By.ID, 'toggleAddBalance')
  REGISTER_BUTTON = (By.XPATH, '//button[text()="Cadastrar"]')

  def register_user(self, email, name, password):
    self.click(*LoginPage.REGISTER_BUTTON)
    self.enter_text(*self.EMAIL_INPUT, email)
    self.enter_text(*self.NAME_INPUT, name)
    self.enter_text(*self.PASSWORD_INPUT, password)
    self.enter_text(*self.PASSWORD_CONFIRMATION_INPUT, password)
    self.click(*self.TOGGLE_BALANCE)
    self.click(*self.REGISTER_BUTTON)
