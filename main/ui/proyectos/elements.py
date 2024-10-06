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
        return self.page.locator(self.selectors.SELEC_PLANTILLA)
    
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
    
    def get_agregar_a_plantilla(self):
        return self.page.locator(self.selectors.AGREGAR_PLANTILLA_BUTTON)
    
    def get_ver_mis_plantillas(self):
        return self.page.locator(self.selectors.MIS_PLANTILLAS)
    
    def get_cerrar_ventana(self):
        return self.page.locator(self.selectors.CERRAR_BUTTON)
    
    def get_nombre_seccion(self):
        return self.page.locator(self.selectors.NOMBRE_SECCION)
    
    def get_agregar_seccion(self):
        return self.page.locator(self.selectors.AGREGAR_SECCION_BUTTON)
    
    def get_agregar_desc_plantilla(self):
        return self.page.locator(self.selectors.DESC_PLANTILLA)
    
    def get_ver_titulo_plantilla(self):
        return self.page.locator(self.selectors.TITULO_PLANTILLA)
    
    def get_ver_plantilla(self):
        return self.page.locator(self.selectors.PLANTILLA)
    
    def get_eliminar_plantilla(self):
        return self.page.locator(self.selectors.ELIMINAR_PLANTILLA_BUTTON)
    
    def get_cerrar_ventana_de_plantilla(self):
        return self.page.locator(self.selectors.CERRAR_VENTANA_PLANTILLA)
    
    def get_ver_msj_confirmacion_plantilla(self):
        return self.page.locator(self.selectors.MSJ_PLANTILLA)
    
    def get_compartir_proyecto(self):
        return self.page.locator(self.selectors.BOTON_COMPARTIR_PROYECTO)
    
    def get_correo_invitado(self):
        return self.page.locator(self.selectors.CAMPO_CORREO_INVITADO)
    
    def get_ver_lista_invitados(self):
        return self.page.locator(self.selectors.LISTA_CORREO_INVITADOS)
    
    def get_selec_correo(self):
        return self.page.locator(self.selectors.SELECT_CORREO_INVITADO)
    
    def get_agregar_invitado(self):
        return self.page.locator(self.selectors.AGREGAR_INVITADO_BUTTON)
    
    def get_msj_invitacion(self):
        return self.page.locator(self.selectors.TEXTO_INVITADO)
    
    def get_clic_fuera(self):
        return self.page.locator(self.selectors.OVERLAY)
    
    def get_clic_menu_proyecto_exportar(self):
        return self.page.locator(self.selectors.EXPORTAR_MENU)
    
    def get_titulo_mjs_exportar(self):
        return self.page.locator(self.selectors.TITULO_MSJ_EXPORTAR_COMO)
    
    def get_clic_boton_exportar(self):
        return self.page.locator(self.selectors.EXPORTAR_BUTTON)
    