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
    
    def get_plantilla(self):
        return self.page.locator(self.selectors.PLANTILLA)
    
    def get_titulo_plantilla(self):
        return self.page.locator(self.selectors.TITULO_PLANTILLA)
    
    def get_copiar_plantilla(self):
        return self.page.locator(self.selectors.COPIAR_PLANTILLA)

    def get_agregar_a_favoritos(self):
        return self.page.locator(self.selectors.ADD_FAVORITOS)
    
    def get_ver_proy_favoritos(self):
        return self.page.locator(self.selectors.PROYECTOS_FAVORITOS)
    
    def get_ver_lista_proyectos(self):
        return self.page.locator(self.selectors.LISTA_PROYECTOS)
    
    def get_ver_proyecto_con_nombre(self):
        return self.page.locator(self.selectors.NOMBRE_PROYECTO)
    
    def get_select_proyecto(self):
        return self.page.locator(self.selectors.PROYECTO)
    
    def get_proyecto_menu(self):
        return self.page.locator(self.selectors.PROYECTO_MENU_BUTTON)
   
    def get_editar_button(self):
        return self.page.locator(self.selectors.EDITAR_BUTTON)
    
    def get_titulo_form_editar(self):
        return self.page.locator(self.selectors.TITULO_FORM_EDITAR)
    
    def get_color_nuevo(self):
        return self.page.locator(self.selectors.COLOR_NUEVO)
    
    def get_selec_vista(self):
        return self.page.locator(self.selectors.PANEL)

    def get_archivar_button(self):
        return self.page.locator(self.selectors.ARCHIVAR_BUTTON)
    
    def get_titulo_msj_archivar_proy(self):
        return self.page.locator(self.selectors.TITULO_VENTANA_ARCHIVAR)
    
    def get_confirmar(self):
        return self.page.locator(self.selectors.MSJ_CONFIRMACION_BUTTON)
    
    def get_eliminar_button(self):
        return self.page.locator(self.selectors.ELIMINAR_BUTTON)
    
    def get_titulo_msj_eliminar_proy(self):
        return self.page.locator(self.selectors.TITULO_VENTANA_ELIMINAR)