import json
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # Localizadores
    USERNAME_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Acessar"]')
    REGISTER_BUTTON = (By.XPATH, '//button[text()="Registrar"]')
    REQUIREMENTS_LINK = (By.XPATH, '//a[text()="Conheça nossos requisitos"]')
    MODAL_TEXT = (By.ID, "modalText")

    def __init__(self, driver):
      # Passa o caminho específico para a página de login
      super().__init__(driver, path="")

    def open_login_page(self):
        self.open(self.URL)

    def login(self, username, password):
        self.enter_text(*self.USERNAME_INPUT, username)
        self.enter_text(*self.PASSWORD_INPUT, password)
        self.click(*self.LOGIN_BUTTON)

    def get_message(self):
        message_element = self.find_element(*self.MODAL_TEXT)
        return message_element.text.strip() if message_element else ""

    def set_local_storage_data(self, name, email):
        # Define os dados do usuário no local storage
        user_data = {
            "name": name,
            "email": email,
            "password": "123",
            "accountNumber": "799-0",
            "balance": 0,
            "logged": True
        }

        self.set_local_storage(email, json.dumps(user_data))