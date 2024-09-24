import logging
from playwright.sync_api import Page
from main.ui.tareas.elements import TareasPageElements

# Configurar el logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TaskPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = TareasPageElements(page)

    #acciones
    def agregar_etiquetas(self):
        logger.info("seleccionar etiqueta")
        self.elements.get_add_etiqueta_button().click()
        self.elements.get_selec_etiquetas().click()
        self.elements.get_clic_fuera().click()
        logger.info("Etiqueta seleccionada ")

    def agregar_prioridad(self):
        logger.info("Prioridad seleccionada")
        self.elements.get_add_menu_prioridad().click()
        self.elements.get_selec_prioridad().click()
    
    def agregar_fecha(self):
        logger.info("fecha vencimiento seleccionada")
        self.elements.get_abrir_fvenc_button().click()
        self.elements.get_selec_fvenc_button().click()

    def agregar_a(self):
        logger.info("añadir a...")
        self.elements.get_selec_a_button().click()
        self.elements.get_menu_proyectos()
        self.elements.get_select_proyecto().click()
    
    def verificar_msj(self):
        self.page.wait_for_selector('[data-testid="toasts-container"]', state='visible', timeout=3000)
        # Tomar una captura de pantalla del mensaje
        self.page.screenshot(path='alerta_aparece.png')
        self.page.goto("https://app.todoist.com/app/inbox")


    def agregar_tarea_bandeja(self, nombre:str, desc:str):
        self.elements.get_add_tarea_button().click()
        logger.info("abrir form agregar tarea, introducir datos")
        self.elements.get_nombre_tarea().fill(nombre)
        self.elements.get_desc_tarea().fill(desc)
        self.agregar_etiquetas()
        logger.info("prioridad")
        self.agregar_prioridad()
        logger.info("por defecto fecha hoy")
        self.elements.get_ver_proyecto()
        logger.info("clic boton")
        self.elements.get_submit_button().click()
        logger.info("se añadio tarea, bandeja de entrada")
        self.verificar_msj()
        
    def agregar_tarea_con_fvenc(self, nombre:str, desc:str):
        self.elements.get_add_tarea_button().click()
        logger.info("abrir form agregar tarea, introducir datos")
        self.elements.get_nombre_tarea().fill(nombre)
        self.elements.get_desc_tarea().fill(desc)
        self.agregar_etiquetas()
        logger.info("prioridad")
        self.agregar_prioridad()
        self.agregar_fecha()

        self.elements.get_ver_proyecto()
        logger.info("clic boton")
        self.elements.get_submit_button().click()
        logger.info("se añadio tarea, bandeja de entrada")
        self.verificar_msj()
        
    def agregar_tarea_en_proyecto(self, nombre:str, desc:str):
        self.elements.get_add_tarea_button().click()
        logger.info("abrir form agregar tarea, introducir datos")
        self.elements.get_nombre_tarea().fill(nombre)
        self.elements.get_desc_tarea().fill(desc)
        self.agregar_etiquetas()
        logger.info("prioridad")
        self.agregar_prioridad()
        self.agregar_fecha()
        self.agregar_a()
        self.elements.get_submit_button().click()
        self.verificar_msj()
        logger.info("tarea añadida a proyecto")
    
    def agregar_tarea_desde_proyecto(self, nombre:str, desc:str):
        # self.elements.get_add_tarea_button().click()
        self.elements.get_select_proyecto_1().click()
        self.elements.get_add_task_project().click()
        logger.info("abrir form agregar tarea, introducir datos")
        self.elements.get_nombre_tarea().fill(nombre)
        self.elements.get_desc_tarea().fill(desc)
        self.agregar_etiquetas()
        logger.info("prioridad")
        self.agregar_prioridad()
        self.agregar_fecha()
        # self.agregar_a()
        self.elements.get_submit_button().click()
        self.verificar_msj()
        logger.info("tarea añadida a proyecto")
    
    def mover_tarea(self, nombre:str, desc:str):
        logger.info("crear tarea en seccion Pendiente")
        self.elements.get_select_proyecto_1().click()
        self.elements.get_add_task_section().click()
        logger.info("abrir form agregar tarea, introducir datos")
        self.elements.get_nombre_tarea().fill(nombre)
        self.elements.get_desc_tarea().fill(desc)
        self.agregar_etiquetas()
        self.agregar_prioridad()
        self.agregar_fecha()
        self.elements.get_submit_button().click()
        logger.info("tarea añadida a seccion")
        logger.info("abrir menu tarea y mover tarea")
        self.elements.get_cancelar_agregar_tarea().click()
        self.elements.get_abrir_menu_tarea().click()
        self.elements.get_mover_tarea().click()
        self.elements.get_selec_seccion_proy().click()
        self.elements.get_msj_alerta_mover_tarea()
        self.page.screenshot(path='mover_tarea.png')
        self.page.wait_for_timeout(1000)
        logger.info("la tarea se movio de seccion: pendiente a en proceso")
    
    def actualizar_info(self):
        logger.info("actualizar la informacion de tarea")
        self.page.goto("https://app.todoist.com/app/inbox")
        self.elements.get_abrir_menu_tarea().click()
        self.elements.get_editar_tarea().click()
        self.elements.get_abrir_fvenc_button().click()
        self.elements.get_selec_nueva_fecha().click()
        self.elements.get_submit_button().click()
        self.page.screenshot(path='actualizar_fecha_tarea.png')
        logger.info("tarea actualizada")
    
    def eliminar(self):
        logger.info("eliminar tarea")
        self.page.goto("https://app.todoist.com/app/inbox")
        self.elements.get_abrir_menu_tarea().click()
        self.elements.get_eliminar_tarea().click()
        self.elements.get_msj_alerta_eliminar_tarea()
        self.page.screenshot(path='eliminar_tarea.png')
        self.elements.get_eliminar_tarea_button().click()
        logger.info("tarea eliminada")