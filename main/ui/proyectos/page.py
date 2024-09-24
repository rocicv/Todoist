import logging

from playwright.sync_api import Page
from main.ui.proyectos.elements import ProyectosPageElements

# Configurar el logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProyectPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = ProyectosPageElements(page)

    #acciones
    def seleccionar_color_magenta(self):
        self.elements.get_select_color().click()
        logger.info("selecciono color")
        self.page.wait_for_timeout(1000)
        self.elements.get_color().click()

    def seleccionar_color_celeste(self):
        self.elements.get_select_color().click()
        logger.info("selecciono color")
        self.page.wait_for_timeout(1000)
        self.elements.get_color_nuevo().click() 

    def verificar_url_contiene(self, expected_url_part: str):
        logger.info(f"Verificar que la URL contiene: {expected_url_part}")
        assert expected_url_part in self.page.url, f"La URL actual no contiene '{expected_url_part}'. URL actual: {self.page.url}"

    def agregar_proyecto(self, titulo:str):
        logger.info("introduciendo datos de proyecto")
        self.elements.get_titulo_espacio_trabajo()
        self.elements.get_proyecto_button().click()
        self.elements.get_menu_popup().click()
        self.elements.get_titulo_form()
        logger.info("introducir datos proyecto")
        self.elements.get_name_input().fill(titulo)
        self.seleccionar_color_magenta()
        self.elements.get_submit_button().click()
        logger.info("proyecto añadido")
        self.elements.get_contend_proy()
        self.page.wait_for_url(f"**/project/**")
        self.verificar_url_contiene("https://app.todoist.com/app/project/")


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
        logger.info("hacer clic en plantilla")
        self.elements.get_plantilla().click()
        self.elements.get_copiar_plantilla().click()
        logger.info("proyecto añadido")
        self.elements.get_contend_proy()
        self.page.wait_for_url(f"**/project/**")
        self.verificar_url_contiene("https://app.todoist.com/app/project/")

    def ver_contar_proyectos(self, titulo:str):
        logger.info("ver cuantos proyectos existen con el mismo nombre")
        self.elements.get_ver_lista_proyectos()
         # Seleccionar todos los elementos que contienen nombres de proyectos
        proyectos = self.page.query_selector_all('#projects_list  li[data-type="project_list_item"] a > div > span')
        # Recoger los textos de los proyectos
        nombres_proyectos = [proyecto.text_content() for proyecto in proyectos]
         # Filtrar y contar cuántos proyectos tienen el mismo nombre que 'titulo'
        cantidad = sum(1 for nombre in nombres_proyectos if nombre.strip() == titulo)
        logger.error(f"Cantidad de proyectos con el nombre '{titulo}': {cantidad}")
        return cantidad

    def añadir_a_favorito(self, titulo:str):
        logger.info("introduciendo datos de proyecto")
        self.elements.get_titulo_espacio_trabajo()
        self.elements.get_proyecto_button().click()
        self.elements.get_menu_popup().click()
        self.elements.get_titulo_form()
        self.elements.get_name_input().fill(titulo)
        self.seleccionar_color_magenta()
        self.page.wait_for_timeout(1000) 
        logger.info("seleccionar campo favoritos")
        self.elements.get_agregar_a_favoritos().check(force=True)
        self.elements.get_submit_button().click()
        logger.info("proyecto añadido a favoritos")
        self.elements.get_ver_proy_favoritos()
        self.page.wait_for_url(f"**/project/**")
        self.verificar_url_contiene("https://app.todoist.com/app/project/")

    def actualizar_info(self):
        logger.info("actualizando color y vista de proyecto")
        self.elements.get_titulo_espacio_trabajo()
        self.elements.get_select_proyecto().click()
        self.elements.get_proyecto_menu().click()
        self.elements.get_editar_button().click()
        self.elements.get_titulo_form()
        logger.info("cambiar datos")
        self.elements.get_name_input()
        self.seleccionar_color_celeste()
        self.elements.get_selec_vista().click()
        self.elements.get_submit_button().click()
        logger.info("proyecto modificado")
        self.elements.get_contend_proy()
        self.page.wait_for_url(f"**/project/**")
        self.verificar_url_contiene("https://app.todoist.com/app/project/")

    def archivar(self):
        logger.info("archivar proyecto")
        self.elements.get_titulo_espacio_trabajo()
        self.elements.get_select_proyecto().click()
        self.elements.get_proyecto_menu().click()
        self.elements.get_archivar_button().click()
        self.elements.get_titulo_msj_archivar_proy()
        self.page.screenshot(path='archivar_proyecto.png')
        self.elements.get_confirmar().click()
        logger.info(" proyecto archivado")
    
    def eliminar(self):
        logger.info("eliminar proyecto")
        self.elements.get_titulo_espacio_trabajo()
        self.elements.get_select_proyecto().click()
        self.elements.get_proyecto_menu().click()
        self.elements.get_eliminar_button().click()
        self.elements.get_titulo_msj_eliminar_proy()
        self.page.screenshot(path='eliminar_proyecto.png')
        self.elements.get_confirmar().click()
        logger.info(" proyecto eliminado")
