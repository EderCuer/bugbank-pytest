import pytest
from faker import Faker
from selenium import webdriver
from pages.login_page import LoginPage
from pages.account_page import AccountPage

fake = Faker()

@pytest.fixture
def driver():
  driver = webdriver.Chrome()
  yield driver
  driver.quit()

def test_invalid_login(driver):
  # Setup
  login_page = LoginPage(driver)
  login_page.open()

  # Act
  login_page.login(fake.email(), "invalid_pass")
  error_message = login_page.get_message()

  # Assert
  assert "Usuário ou senha inválido." in error_message

def test_valid_login(driver):
  # Setup
  name = fake.name()
  email = fake.email()
  login_page = LoginPage(driver)
  account_page = AccountPage(driver)
  login_page.open() 
  login_page.set_local_storage_data(name, email)

  # Act
  login_page.login(email, "123")
  user_welcome = account_page.get_welcome_message()

  # Assert
  assert  f"Olá {name}," in user_welcome
