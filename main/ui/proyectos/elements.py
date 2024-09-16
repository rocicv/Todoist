from playwright.sync_api import Page
from main.ui.proyectos.selectors import ProyectosPageSelectors

class ProyectosPageElements:
    def __init__(self, page: Page):
        self.page = page
        self.selectors = ProyectosPageSelectors()
    
    def get_titulo_espacio_trabajo(self):
        return self.page.locator(self.selectors.TITULO_ESPACIO_TRABAJO)
    
    def get_proyecto_button(self):
        return self.page.locator(self.selectors.PROYECTOS_BUTTON)
    
    def get_menu_popup(self):
        return self.page.locator(self.selectors.MENU_POPUP)
    
    def get_titulo_form(self):
        return self.page.locator(self.selectors.TITULO_FORMULARIO)
    
    def get_name_input(self):
        return self.page.locator(self.selectors.CAMPO_NOMBRE)
    
    def get_select_color(self):
        return self.page.locator(self.selectors.SELECT_COLOR)
    
    def get_ver_color(self):
        return self.page.locator(self.selectors.VER_COLOR).is_visible()
    
    def get_color(self):
        return self.page.locator(self.selectors.COLOR)
    
    def get_submit_button(self):
        return self.page.locator(self.selectors.SUBMIT_BUTTON)
    
    def get_contend_proy(self):
        return self.page.locator(self.selectors.CONTENEDOR_PROYECTO)
    
    def get_menu_plantilla(self):
        return self.page.locator(self.selectors.EXPLORAR_PLANTILLAS)
    
    def get_nombre_categoria(self):
        return self.page.locator("#\\/app\\/templates\\/category\\/personal")
    
    def get_plantilla(self):
        return self.page.locator(self.selectors.PLANTILLA)
    def get_titulo_plantilla(self):
        return self.page.locator(self.selectors.TITULO_PLANTILLA)
    def get_copiar_plantilla(self):
        return self.page.locator(self.selectors.COPIAR_PLANTILLA)
    