# main/login_page.py
import logging
from playwright.sync_api import Page
from main.ui.login.elements import LoginPageElements

# Configurar el logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = LoginPageElements(page)

    # Acciones
    def ingresar_valores(self, email:str, password:str):
        logger.info("ingresando credenciales")
        self.elements.get_email_input().fill(email)
        self.elements.get_password_input().fill(password)
        self.elements.get_submit_button().click()

    def wait_for_dashboard(self, timeout=7000):
        logger.info("Verificando que se encuentre en la página de today")
        
        expected_url = self.elements.get_dashboard_url()

        try:
            # Esperar hasta que la URL sea la esperada (puedes ajustar el timeout)
            self.page.wait_for_url(expected_url, timeout=timeout)
            
            if self.page.url == expected_url:
                logger.info("Inicio de sesión exitoso, estás en la página de today")
            else:
                logger.error(f"No se ha iniciado sesión correctamente. URL actual: {self.page.url}")
                # Aquí se puede llamar al método msj_error() si no se encuentra en la URL correcta
                # self.msj_error()
        
        except Exception as e:
            logger.error(f"Error al verificar la URL del dashboard: {e}")
            # Manejar el error y llamar al método msj_error() en caso de excepción
            self.msj_error()
    
    def logout(self):  # cerrar sesion 
        logger.info("abrir menu configuracion")
        self.elements.get_menu_conf().click()
        logger.info("hacer clic boton cerrar sesion")
        self.elements.get_cerrar_sesion().click()
        self.page.wait_for_timeout(3000)
        logger.info("Logout completado")
        self.page.wait_for_url("https://app.todoist.com/auth/login")


    def msj_error(self):
        logger.error("No se pudo iniciar sesión, mostrando mensaje de error")
        # Aquí puedes realizar alguna acción adicional, como interactuar con un mensaje de error en la página
        error_visible =self.elements.get_msj_error()
        logger.info("mensaje error: Email o contraseña incorrectos")


