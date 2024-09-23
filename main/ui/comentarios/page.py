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
        
        logger.info(f"URL actual: {self.page.url}")
        logger.info('ingresando al metodo comentar tarea')
        self.elements.get_abrir_tarea().click()
        logger.info("hacer clic campo comentario")
        self.elements.get_abrir_campo_comentario().click()
        logger.info("introduciendo datos")
        self.elements.get_introducir_comentario().fill(comentario)
        self.elements.get_submit_button().click()
        logger.info("comentario realizado")
        self.elements.get_cerrar_tarea().click()
        self.eliminar_comentario()
    

    def eliminar_comentario(self):
        logger.info("abrir tarea")
        self.elements.get_abrir_tarea().click()
        self.elements.get_select_comentario()
        logger.info("abrir comentario")
        self.page.wait_for_timeout(1000) 
        self.elements.get_abrir_menu_comentario().click()
        logger.info("click eliminar")
        self.elements.get_eliminar_comentario().click()
        self.elements.get_ver_msj_alerta()
        self.page.screenshot(path='alerta_eliminar_comentario.png')
        self.elements.get_aceptar_eliminar().click()
        logger.info("comentario eliminado")


