import logging
from urllib.parse import quote_plus

from playwright.sync_api import Page
# from main.ui.login.elements import LoginPageElements
from main.ui.proyectos.elements import ProyectosPageElements

# Configurar el logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProyectPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = ProyectosPageElements(page)

    #acciones
    def agregar_proyecto(self, titulo:str):
        logger.info("introduciendo datos de proyecto")
        self.elements.get_titulo_espacio_trabajo()
        self.elements.get_proyecto_button().click()
        self.elements.get_menu_popup().click()
        self.elements.get_titulo_form()
        logger.info("introducir datos proyecto")
        self.elements.get_name_input().fill(titulo)
        self.elements.get_select_color().click()
        logger.info("seleccionar color magenta")
        self.page.wait_for_timeout(1000) 
        self.elements.get_color().click()
        self.elements.get_submit_button().click()
        logger.info("proyecto añadido")
        self.elements.get_contend_proy()
        self.page.wait_for_url(f"**/project/**")
        expected_url_part = "https://app.todoist.com/app/project/"
        logger.info(f"Verificar que la URL contiene: {expected_url_part}")
        assert expected_url_part in self.page.url, f"La URL actual no contiene '{expected_url_part}'. URL actual: {self.page.url}"


    def agregar_proyecto_plantilla(self):
        logger.info("agregando proyecto a partir de una plantilla")
        self.elements.get_titulo_espacio_trabajo()
        self.elements.get_proyecto_button().click()
        logger.info("menu plantillas")
        self.elements.get_menu_plantilla().click()
        expected_url_part = "https://app.todoist.com/app/templates/category/my-templates"
        self.page.wait_for_url(f"**/templates/category/my-templates")
        logger.info(f"Verificar que la URL contiene: {expected_url_part}")
        self.page.wait_for_timeout(1000) 
        self.elements.get_nombre_categoria().click()
        self.elements.get_plantilla().click()
        # logger.info("Verificando que el nombre de la plantilla sea 'Seguimiento de objetivos'")
        self.elements.get_copiar_plantilla().click()
        logger.info("proyecto añadido")
        self.elements.get_contend_proy()
        self.page.wait_for_url(f"**/project/**")
        expected_url_part = "https://app.todoist.com/app/project/"
        logger.info(f"Verificar que la URL contiene: {expected_url_part}")
        assert expected_url_part in self.page.url, f"La URL actual no contiene '{expected_url_part}'. URL actual: {self.page.url}"

