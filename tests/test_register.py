import pytest
import re
from faker import Faker
from selenium import webdriver
from pages.login_page import LoginPage
from pages.register_page import RegisterPage

fake = Faker()

@pytest.fixture
def driver():
  driver = webdriver.Chrome()
  yield driver
  driver.quit()

def test_register_user(driver):
  # Setup
  email = fake.email()
  name = fake.name()
  password = '123'

  login_page = LoginPage(driver)
  register_page = RegisterPage(driver)
  login_page.open()

  # Act
  register_page.register_user(email, name, password)
  create_account_message = login_page.get_message()
  pattern = r"A conta \d+-\d foi criada com sucesso"

  # Assert
  assert re.search(pattern, create_account_message), "A mensagem não corresponde ao padrão esperado."
