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
        self.elements.get_abrir_proyecto().click()
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
        

    def eliminar_comentario_proyecto(self):
        logger.info("abrir menu")
        self.elements.get_abrir_bandeja_comentario().click()
        self.elements.get_abrir_menu_comentario().click()
        self.elements.get_eliminar_comentario().click()
        self.elements.get_ver_msj_alerta()
        self.page.screenshot(path='utils/img/alerta_eliminar_comentario.png')
        self.elements.get_aceptar_eliminar().click()
        logger.info("comentario eliminado")

    def actualizar_info(self, comentario):
        logger.info('actualizar comentario')
        self.elements.get_abrir_tarea().click()
        self.elements.hover_select_comentario()
        self.elements.get_abrir_menu_comentario().click()
        self.elements.get_editar_comentario().click()
        self.elements.get_actualizar_comentario().fill(comentario)
        self.elements.get_confirmar_actualizar_comentario().click()
        logger.info("comentario actualizado")
    
    def reaccionar_comment_tarea(self):
        logger.info("reaccionar a comentario")
        self.elements.get_abrir_tarea().click()
        self.elements.get_select_comentario().is_visible()
        self.elements.get_agregar_reaccion_emoji().click()#abrir menu
        logger.info("select emoji encontrado")
        self.page.wait_for_selector('div[data-testid="Usadas recientemente"]', timeout=9000)
        logger.info("Emojis recientes visibles")
        emoji_selector = 'div[data-testid="Usadas recientemente"] div[title="botón de marca de verificación"]'
        self.page.locator(emoji_selector).wait_for(state='visible', timeout=5000)
        self.page.locator(emoji_selector).click(force=True, timeout=4000)
        logger.info("Emoji seleccionado")
        self.elements.get_ver_reacciones()
        self.page.wait_for_timeout(200)
        self.page.screenshot(path='utils/img/reaccion_a_comentario.png')
        logger.info("reaccion realizada")
        # self.elements.get_cerrar_tarea().click()
    

    def reaccionar_otra_vez(self):
        logger.info("reaccionar otra vez a comentario")
        # self.elements.get_abrir_tarea().click()
        self.elements.get_select_comentario().is_visible()
        self.elements.get_agregar_reaccion_emoji().click()#abrir menu
        logger.info("select emoji encontrado")
        # self.page.wait_for_selector('div[data-testid="Usadas recientemente"]', timeout=9000)
        logger.info("Emojis recientes visibles")
        emoji_selector = 'div[data-testid="Usadas recientemente"] div[title="botón de marca de verificación"]'
        self.page.locator(emoji_selector).wait_for(state='visible', timeout=5000)
        logger.info("clic emoji")
        self.page.locator(emoji_selector).click(force=True, timeout=4000)
        logger.info("Emoji seleccionado")
        # self.elements.get_ver_reacciones()
        self.page.wait_for_timeout(200)
        self.page.screenshot(path='utils/img/reaccion_eliminada.png')
        logger.info("reaccion eliminada")
    
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