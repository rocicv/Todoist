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
        logger.info(f"verificar que la URL contiene: {expected_url_part}")
        assert expected_url_part in self.page.url, f"la URL actual no contiene '{expected_url_part}'. URL actual: {self.page.url}"

    def agregar_proyecto(self, titulo:str):
        logger.info("introduciendo datos de proyecto")
        self.elements.get_titulo_espacio_trabajo()
        self.elements.get_proyecto_button().click()
        self.elements.get_menu_popup().click()
        self.elements.get_titulo_form()
        self.elements.get_name_input().fill(titulo)
        self.seleccionar_color_magenta()
        self.elements.get_submit_button().click()
        logger.info("proyecto añadido")
        self.elements.get_contend_proy()
        self.page.wait_for_timeout(1000) 
        self.page.wait_for_url(f"**/project/**")
        self.verificar_url_contiene("https://app.todoist.com/app/project/")


    def agregar_proyecto_plantilla(self):
        logger.info("agregando proyecto a partir de una plantilla")
        self.elements.get_titulo_espacio_trabajo()
        self.elements.get_proyecto_button().click()
        self.elements.get_menu_plantilla().click()
        expected_url_part = "https://app.todoist.com/app/templates/category/my-templates"
        self.page.wait_for_url(f"**/templates/category/my-templates")
        logger.info(f"Verificar que la URL contiene: {expected_url_part}")
        self.page.wait_for_timeout(1000) 
        self.elements.get_plantilla().click()
        self.elements.get_copiar_plantilla().click()
        logger.info("proyecto añadido")
        self.elements.get_contend_proy()
        self.page.wait_for_url(f"**/project/**")
        self.verificar_url_contiene("https://app.todoist.com/app/project/")

    def eliminar_plantilla(self):
        self.elements.get_ver_plantilla().is_visible()
        self.elements.get_ver_plantilla().click()
        self.page.wait_for_timeout(500) 
        self.elements.get_eliminar_plantilla().click()
        self.page.screenshot(path='utils/img/eliminar_plantilla_de_proyecto.png')
        self.elements.get_confirmar().click()
        logger.info("se elimino la platilla")
        self.elements.get_cerrar_ventana_de_plantilla().is_visible(timeout=200)
        self.elements.get_cerrar_ventana_de_plantilla().click()

    def crear_platilla(self, desc):
        logger.info("creando plantilla a partir de proyecto")
        self.elements.get_proyecto_menu().is_visible()
        self.elements.get_proyecto_menu().click()
        self.elements.get_agregar_a_plantilla().click()
        self.elements.get_agregar_desc_plantilla().fill(desc)
        self.elements.get_confirmar().click()
        expected_url = "https://app.todoist.com/app/templates/category/my-templates"
        self.page.wait_for_url(expected_url)
        self.elements.get_ver_msj_confirmacion_plantilla()
        self.elements.get_ver_mis_plantillas()
        self.page.wait_for_selector('div[aria-labelledby="my-project-templates-header"] a')
        self.elements.get_ver_titulo_plantilla()
        self.page.screenshot(path='utils/img/plantilla_de_proyecto.png')
        logger.info("mi plantilla ha sido creada")
        self.eliminar_plantilla()
    
    def agregar_seccion(self):
        secciones = ["Pendiente", "En proceso", "Terminado"]
        
        for seccion in secciones:
            self.elements.get_proyecto_menu().is_visible()
            self.elements.get_proyecto_menu().click()
            self.elements.get_agregar_seccion().click()
            # Selecciona el campo donde quieres hacer el fill
            self.elements.get_nombre_seccion().click()  
            self.elements.get_nombre_seccion().fill(seccion)
            self.elements.get_submit_button().click()
            # Espera alguna confirmación o cambio en la página si es necesario
        self.page.wait_for_selector(f'text={seccion}')  # Espera que aparezca la sección que acabas de crear
        logger.info("seccion creada")

    def añadir_a_favorito(self):
        logger.info("introduciendo datos de proyecto")
        self.elements.get_proyecto_menu().is_visible()
        self.elements.get_proyecto_menu().click()
        self.elements.get_agregar_a_favoritos().click()
        logger.info("proyecto añadido a favoritos")
        self.elements.get_ver_proy_favoritos()
        self.page.wait_for_url(f"**/project/**")
        self.verificar_url_contiene("https://app.todoist.com/app/project/")

    def actualizar_info(self):
        logger.info("actualizando color y vista de proyecto")
        self.elements.get_proyecto_menu().is_visible()
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
        self.page.screenshot(path='utils/img/archivar_proyecto.png')
        self.elements.get_confirmar().click()
        logger.info("proyecto archivado")
    
    def eliminar(self):
        logger.info("eliminar proyecto")
        self.elements.get_proyecto_menu().is_visible()
        self.elements.get_proyecto_menu().click()
        self.page.wait_for_timeout(500)
        self.elements.get_eliminar_button().click()
        self.elements.get_titulo_msj_eliminar_proy()
        self.page.screenshot(path='utils/img/eliminar_proyecto.png')
        self.elements.get_confirmar().click()
        logger.info("proyecto eliminado")
    
    def compartir_proyecto(self, correo):
        logger.info("compartir proyecto por correo")
        self.elements.get_compartir_proyecto().click() #abrir menu compartir
        self.elements.get_correo_invitado().fill(correo)
        self.elements.get_ver_lista_invitados().is_visible()
        self.elements.get_selec_correo().click()
        self.elements.get_agregar_invitado().click()
        self.elements.get_msj_invitacion()#ver mensaje de confirmacion
        self.page.screenshot(path='utils/img/invitar_a_proyecto.png')
        logger.info("invitacion enviada")
        self.elements.get_clic_fuera().click()
    
    def exportar(self):
        logger.info("exportar proyecto cvs")
        self.elements.get_proyecto_menu().click()
        logger.info("exportar")
        self.elements.get_clic_menu_proyecto_exportar().click()
        logger.info("captura")
        self.elements.get_titulo_mjs_exportar()
        self.page.screenshot(path='utils/img/proyecto_exportado.png')
        logger.info("captura, confirmar exportar")
        self.elements.get_clic_boton_exportar().click()
        logger.info("proyecto exporto")
        
