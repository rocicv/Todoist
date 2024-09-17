from playwright.sync_api import Page
from main.ui.tareas.selectors import TareasPageSelectors

class TareasPageElements:
    def __init__(self, page: Page):
        self.page = page
        self.selectors = TareasPageSelectors()
    
    def get_add_tarea_button(self):
        return self.page.locator(self.selectors.ADD_TAREA_BUTTON)
    def get_nombre_tarea(self):
        return self.page.locator(self.selectors.NOMBRE_TAREA)
    def get_desc_tarea(self):
        return self.page.locator(self.selectors.DESC_TAREA)
    
    def get_add_etiqueta_button(self):
        return self.page.locator(self.selectors.ETIQUETA_BUTTON)
   
    def get_selec_etiquetas(self):
        return self.page.locator(self.selectors.ETIQUETA)
        
    def get_clic_fuera(self):
        return self.page.locator(self.selectors.POPPER_OVERLAY)
        
    
    def get_add_menu_prioridad(self):
        return self.page.locator(self.selectors.PRIORIDAD_BUTTON)
    def get_selec_prioridad(self):
        return self.page.locator(self.selectors.PRIORIDAD)
    def get_ver_proyecto(self):
        return self.page.locator(self.selectors.PROYECTO)
    def get_submit_button(self):
        return self.page.locator(self.selectors.SUBMIT_BUTTON)
    
    def get_msj_alert(self):
        return self.page.locator(self.selectors.MENSAJE_ALERT)

    def get_badeja_button(self):
        return self.page.locator(self.selectors.BANDEJA_ENTRADA_BUTTON)