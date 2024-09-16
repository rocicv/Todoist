# main/elements.py

from playwright.sync_api import Page
from main.ui.login.selectors import LoginPageSelectors

class LoginPageElements:
    def __init__(self, page: Page):
        self.page = page
        self.selectors = LoginPageSelectors()

    def get_email_input(self):
        return self.page.locator(self.selectors.EMAIL_INPUT)

    def get_password_input(self):
        return self.page.locator(self.selectors.PASSWORD_INPUT)

    def get_submit_button(self):
        return self.page.locator(self.selectors.SUBMIT_BUTTON)

    def get_dashboard_url(self):
        return self.selectors.DASHBOARD_URL

    def get_msj_error(self):
        return self.page.locator(self.selectors.MSJ_ERROR).is_visible()
    
    def get_menu_conf(self):
        return self.page.locator(self.selectors.MENU_CONFIGURACION)
    def get_cerrar_sesion(self):
        return self.page.locator(self.selectors.CERRAR_SESION_BUTTON)
