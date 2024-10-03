import time
from playwright.sync_api import Page
from main.ui.comentarios.selectors import ComentariosPageSelectors

class CommentPageElements:
    def __init__(self, page: Page):
        self.page = page
        self.selectors = ComentariosPageSelectors()

    def get_abrir_proyecto(self):
        return self.page.locator(self.selectors.PROYECTO_BUTTON)
        
    def get_abrir_bandeja_comentario(self):
        return self.page.locator(self.selectors.COMENTARIO_BUTTON)
        
    def get_ver_txt_bandeja_comentario(self):
        return self.page.locator(self.selectors.TEXTO_COMENT_PROY)
        
    def get_introducir_comentario(self):
        return self.page.locator(self.selectors.CAMPO_COMENTARIO)
        
    def get_submit_button(self):
        return self.page.locator(self.selectors.SUBMIT_BUTTON)
        
    def get_ver_comentarios(self):
        return self.page.locator(self.selectors.COMENTARIOS_PROYECTO)
    
    def get_abrir_tarea(self):
        return self.page.locator(self.selectors.ABRIR_TAREA)
    
    def get_cerrar_tarea(self):
        return self.page.locator(self.selectors.CERRAR_TAREA)
    
    def get_abrir_campo_comentario(self):
        return self.page.locator(self.selectors.ABRIR_CAMPO_COMENTARIO)
 
    def get_abrir_menu_comentario(self):
        return self.page.locator(self.selectors.MENU_COMENTARIO)
    
    def get_select_comentario(self):
        return self.page.locator(self.selectors.SELECT_COMENTARIO)
 
    def hover_select_comentario(self, timeout=1000):
        comentario = self.get_select_comentario()
        comentario.hover(timeout=timeout)
        time.sleep(1)

    def get_eliminar_comentario(self):
        return self.page.locator(self.selectors.ELIMINAR_COMENTARIO_BUTTON)
    
    def get_ver_msj_alerta(self):
        return self.page.locator(self.selectors.MENSAJE_ALERTA)
    
    def get_aceptar_eliminar(self):
        return self.page.locator(self.selectors.ACEPTAR_BUTTON)
    
    def get_cancelar_agregar_comentario(self):
        return self.page.locator(self.selectors.CANCELAR_BUTTON)
     
    def get_editar_comentario(self):
        return self.page.locator(self.selectors.EDITAR_BUTTON)
    
    def get_confirmar_actualizar_comentario(self):
        return self.page.locator(self.selectors.ACTUALIZAR_BUTTON)
    
    def get_actualizar_comentario(self):
        return self.page.locator(self.selectors.CAMPO_COMENTARIO_ACTUALIZAR)
    
    def get_agregar_reaccion_emoji(self):
        return self.page.locator(self.selectors.AGREGAR_REACCION)
    
    def get_ver_emoji_reciente(self):
        return self.selectors.EMOJIS_RECIENTES
    
    def get_selec_emoji(self):
        return self.page.locator(self.selectors.EMOJI_VERIFICACION)
    
    def get_ver_reacciones(self):
        return self.page.locator(self.selectors.REACCIONES_LIST)
    
    def get_ver_menu_emoji(self):
        return self.page.locator(self.selectors.MENU_EMOJIS)
    
    def get_ver_subtarea(self):
        return self.page.locator(self.selectors.SUBTAREA)
    
    def get_comentar_subtarea(self):
        return self.page.locator(self.selectors.ICONO_COMENTAR_BUTTON)