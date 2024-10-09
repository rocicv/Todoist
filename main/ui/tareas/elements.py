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
        return self.page.locator(self.selectors.ANADIR_A_BUTTON)
    
    def get_submit_button(self):
        return self.page.locator(self.selectors.SUBMIT_BUTTON)
    
    def get_msj_alert(self):
        return self.page.locator(self.selectors.MENSAJE_ALERT)

    def get_badeja_button(self):
        return self.page.locator(self.selectors.BANDEJA_ENTRADA_BUTTON)
    
    def get_abrir_fvenc_button(self):
        return self.page.locator(self.selectors.DATE_BUTTON)
    
    def get_selec_fvenc_button(self):
        return self.page.locator(self.selectors.DATE)
    
    def get_selec_a_button(self):
        return self.page.locator(self.selectors.SELECT_A_BUTTON)
    
    def get_menu_proyectos(self):
        return self.page.locator(self.selectors.MENU_PROYECTOS)
    
    def get_select_proyecto(self):
        return self.page.locator(self.selectors.PROYECTO)
    
    def get_select_proyecto_1(self):
        return self.page.locator(self.selectors.LISTA_PROYECTOS)
    
    def get_add_task_project(self):
        return self.page.locator(self.selectors.ADD_BUTTON_PROYECT)
    
    def get_add_task_section(self):
        return self.page.locator(self.selectors.ADD_BUTTON_SECTION)
    
    def get_abrir_menu_tarea(self):
        return self.page.locator(self.selectors.MENU_TAREA)
    
    def get_abrir_menu_tarea_seccion(self):
        return self.page.locator(self.selectors.MENU_TAREA_DENTRO_SECCION)
    
    def get_abrir_menu_sub_tarea(self):
        return self.page.locator(self.selectors.MENU_SUB_TAREA)
    
    def get_mover_tarea(self):
        return self.page.locator(self.selectors.MOVER_TAREA_BUTTON)
    
    def get_selec_inbox(self):
        return self.page.locator(self.selectors.INBOX)
    
    def get_selec_seccion_proy(self):
        return self.page.locator(self.selectors.SECCION_PROCESO_PROY)
    
    def get_selec_seccion_inbox(self):
        return self.page.locator(self.selectors.SECCION_PROCESO_INBOX)
    
    def get_msj_alerta_mover_tarea(self):
        return self.page.locator(self.selectors.MENSAJE_ALERT_MOVER_TAREA)
    
    def get_cancelar_agregar_tarea(self):
        return self.page.locator(self.selectors.CANCELAR_BUTTON)
    
    def get_editar_tarea(self):
        return self.page.locator(self.selectors.EDITAR_TAREA_BUTTON)
    
    def get_selec_nueva_fecha(self):
        return self.page.locator(self.selectors.DATE_PROXIMA_SEMANA)
    
    def get_eliminar_tarea(self):
        return self.page.locator(self.selectors.ELIMINAR_TAREA_BUTTON)
    
    def get_msj_alerta_eliminar_tarea(self):
        return self.page.locator(self.selectors.MENSAJE_ALERT_ELIMINAR_TAREA)
    
    def get_eliminar_tarea_button(self):
        return self.page.locator(self.selectors.BUTON_ELIMINAR)
    
    def get_select_tarea(self):
        return self.page.locator(self.selectors.TAREA)
    
    def get_nombre_tarea_n1(self):
        return self.page.locator(self.selectors.NOMBRE_TAREA_N1)
    
    def get_add_subtarea(self):
        return self.page.locator(self.selectors.ADD_SUBTAREA)
    
    def get_cerrar_tarea(self):
        return self.page.locator(self.selectors.CERRAR_TAREA_BUTTON)
    
    def get_select_subtarea(self):
        return self.page.locator(self.selectors.SELECT_SUBTAREA)
    
    def get_retroceder_nivel_subtarea(self):
        return self.page.locator(self.selectors.SUBTAREA_BREARCUMB)
    
    def get_menu_agregar_seccion(self):
        return self.page.locator(self.selectors.MENU_AGREGAR_SECCION)
    def get_campo_seccion(self):
        return self.page.locator(self.selectors.CAMPO_INPUT_SECCION)
    def get_agregar_seccion_submit(self):
        return self.page.locator(self.selectors.AGREGAR_SECCION_BUTTON_SUBMIT)