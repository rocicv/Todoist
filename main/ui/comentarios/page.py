import logging
from playwright.sync_api import Page
from main.ui.comentarios.elements import CommentPageElements

# Configurar el logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CommentPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = CommentPageElements(page)
    
    #acciones
    def agregar_coment_a_proy(self, comentario:str):
        logger.info("Ingresa al metodo")
        # self.elements.get_abrir_proyecto().click()
        self.elements.get_abrir_bandeja_comentario().click()
        logger.info("bandeja de coment")
        self.elements.get_ver_txt_bandeja_comentario()
        logger.info("introduciendo datos")
        self.elements.get_introducir_comentario().fill(comentario)
        self.elements.get_submit_button().click()
        self.elements.get_ver_comentarios()
        logger.info("comentario realizado")

    def agregar_coment_a_tarea(self, comentario:str):
        # logger.info(f"URL actual: {self.page.url}")
        logger.info('ingresando al metodo comentar tarea')
        self.elements.get_abrir_tarea().click()
        self.elements.get_abrir_campo_comentario().click()
        self.elements.get_introducir_comentario().fill(comentario)
        self.elements.get_submit_button().click()
        logger.info("comentario realizado")
        self.elements.get_cancelar_agregar_comentario().click()
        # self.elements.get_cerrar_tarea().click()
    

    def eliminar_comentario(self):
        logger.info("abrir tarea")
        self.elements.hover_select_comentario()
        self.elements.get_abrir_menu_comentario().click()
        self.elements.get_eliminar_comentario().click()
        self.elements.get_ver_msj_alerta()
        self.page.screenshot(path='utils/img/alerta_eliminar_comentario.png')
        self.elements.get_aceptar_eliminar().click()
        logger.info("comentario eliminado")
        self.elements.get_cerrar_tarea().click()
        

    def eliminar_comentario_proyecto(self):
        logger.info("abrir menu")
        # self.elements.get_abrir_bandeja_comentario().click()
        self.elements.get_abrir_menu_comentario().is_visible()
        self.elements.get_abrir_menu_comentario().click()

        self.elements.get_eliminar_comentario().click()
        self.elements.get_ver_msj_alerta()
        self.page.screenshot(path='utils/img/alerta_eliminar_comentario.png')
        self.elements.get_aceptar_eliminar().click()
        logger.info("comentario eliminado")
        self.elements.get_cerrar_ventana().click()

    def actualizar_info(self, comentario):
        logger.info('actualizar comentario')
        # self.elements.get_abrir_tarea().click()
        self.elements.hover_select_comentario()
        self.elements.get_abrir_menu_comentario().click()
        self.elements.get_editar_comentario().click()
        self.elements.get_actualizar_comentario().fill(comentario)
        self.elements.get_confirmar_actualizar_comentario().click()
        logger.info("comentario actualizado")
    
    
    def comment_subtarea(self, comentario):
        logger.info("metodo reaccionar a subtarea")
        self.elements.get_abrir_tarea().click()
        # self.elements.get_abrir_tarea().click()
        self.page.hover('.task_list_item.task_list_item--project_hidden')#subtarea
        self.elements.get_comentar_subtarea().click()
        self.elements.get_introducir_comentario().fill(comentario)
        self.elements.get_submit_button().click()
        logger.info("comentario realizado")
        self.elements.get_cancelar_agregar_comentario().click()
    
    def notificar_coment_proy(self, comentario):
        logger.info("enviar comentario como notificacion")
        self.elements.get_abrir_proyecto().click()
        self.elements.get_abrir_bandeja_comentario().click()
        logger.info("cerrar todos")
        self.page.click('div[data-testid="collaboratorPill"] > svg', force=True)
        logger.info("agregar correo")
        # self.page.screenshot(path='utils/img/eliminar_todos.png')
        self.page.wait_for_timeout(200)
        self.elements.get_campo_notificar().click()
        self.elements.get_selec_correo_notificacion().click()
        logger.info("agregar comentario")
        self.elements.get_introducir_comentario().fill(comentario)
        self.page.screenshot(path='utils/img/comentario_proy_notificar.png')
        self.elements.get_submit_button().click()
        self.elements.get_ver_comentarios()
        logger.info("comentario realizado")

    def notificar_coment_tarea(self, comentario):
        logger.info('ingresando al metodo comentar tarea')
        # self.elements.get_abrir_proyecto().click()
        self.elements.get_abrir_tarea().click()
        self.elements.get_abrir_campo_comentario().click()
        logger.info('agregando correo')
        self.elements.get_campo_notificar().click()
        self.elements.get_selec_correo_notificacion().click()
        logger.info('agregando comentario')
        self.elements.get_introducir_comentario().fill(comentario)
        self.page.screenshot(path='utils/img/comentario_notificar_correo.png')
        self.elements.get_submit_button().click()
        logger.info("comentario realizado")
        self.elements.get_cancelar_agregar_comentario().click()