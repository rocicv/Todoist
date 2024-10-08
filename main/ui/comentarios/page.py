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
        self.elements.hover_select_comentario()
        self.elements.get_abrir_menu_comentario().click()
        self.elements.get_eliminar_comentario().click()
        self.elements.get_ver_msj_alerta()
        self.page.screenshot(path='utils/img/alerta_eliminar_comentario.png')
        self.elements.get_aceptar_eliminar().click()
        logger.info("comentario eliminado")
        self.elements.get_cerrar_ventana().click()
        self.page.wait_for_timeout(500)


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
        logger.info("comentar subtarea")
        self.elements.get_abrir_tarea().click()
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

    
    def reaccionar(self, emoji:str):
        self.elements.get_abrir_tarea().click()
        self.elements.get_select_comentario().is_visible()
        self.elements.get_agregar_reaccion_emoji().click()#abrir menu
        logger.info("buscar emoji")
        # self.page.wait_for_selector('input[aria-label="Buscar emoji"]', state='visible', timeout=3000)
        self.page.wait_for_timeout(300)
        self.elements.get_campo_buscar_emoji().type(emoji)
        self.elements.get_campo_buscar_emoji().press('Enter')
        logger.info("emojis encontrados")
        # self.page.wait_for_timeout(500)
        self.page.screenshot(path='utils/img/emojis.png')
        logger.info("select emoji")
        self.elements.get_ver_emoji_corazon().is_visible()
        self.elements.get_ver_emoji_corazon().click()
        self.page.wait_for_timeout(400)
        self.page.screenshot(path='utils/img/reaccion_emoji.png')
        logger.info("reacciono a un comentario con un emoji")
    
    def reaccionar_segundavez(self):
        # self.elements.get_abrir_tarea().click()
        self.elements.get_select_comentario().is_visible()
        self.elements.get_agregar_reaccion_emoji().click()#abrir menu
        self.page.wait_for_timeout(300)
        logger.info("select emoji igual")
        self.elements.get_ver_emoji_corazon().is_visible()
        self.elements.get_ver_emoji_corazon().click()
        self.page.wait_for_timeout(400)
        self.page.screenshot(path='utils/img/reaccion_eliminado.png')
        raise AssertionError(f"se elimino el emoji de reaccion de un comentario")
    
    def desfasar(self):
        emoji='flor'
        self.elements.get_abrir_tarea().click()
        self.elements.get_select_comentario().is_visible()
        self.elements.get_agregar_reaccion_emoji().click()#abrir menu
        logger.info("buscar emoji")
        # self.page.wait_for_selector('input[aria-label="Buscar emoji"]', state='visible', timeout=3000)
        self.page.wait_for_timeout(300)
        self.elements.get_campo_buscar_emoji().type(emoji)
        self.elements.get_campo_buscar_emoji().press('Enter')
        logger.info("emojis encontrados")
        self.page.wait_for_timeout(500)
        self.page.screenshot(path='utils/img/emojis_resultado.png')
        logger.info("select emoji")
        for i in range(1, 13):
            try:
                emoji_selector = f'[data-testid="emojiWrapper"] > div > div:nth-of-type({i})'
                self.page.is_visible(emoji_selector)
                self.page.click(emoji_selector)
                logger.info(f"Clic realizado en: {emoji_selector}")
                self.elements.get_agregar_reaccion_emoji().click()
            except Exception as e:
                logger.info(f"No se encontró el emoji en la posición {i}: {e}")
                break  # Salir del bucle si no hay más emojis
        
        self.page.press('Body','Escape')
        self.page.wait_for_timeout(400)
        self.page.screenshot(path='utils/img/reaccion_emojis_desfase.png')
        raise AssertionError(f"reacciono a un comentario con muchos emojis que desfasan dentro del div comentarios")