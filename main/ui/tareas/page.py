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
        self.page.screenshot(path='utils/img/alerta_aparece.png')
        # self.page.goto("https://app.todoist.com/app/inbox")


    def agregar_tarea_bandeja(self, nombre:str, desc:str):
        self.elements.get_add_tarea_button().click()
        logger.info("abrir form agregar tarea, introducir datos")
        self.elements.get_nombre_tarea().fill(nombre)
        self.elements.get_desc_tarea().fill(desc)
        self.agregar_etiquetas()
        self.agregar_prioridad()
        # logger.info("por defecto fecha hoy")
        self.elements.get_ver_proyecto()
        self.elements.get_submit_button().click()
        logger.info("se añadio tarea, bandeja de entrada")
        self.verificar_msj()
        
    def agregar_tarea_con_fvenc(self, nombre:str, desc:str):
        self.elements.get_add_tarea_button().click()
        logger.info("abrir form agregar tarea, introducir datos")
        self.elements.get_nombre_tarea().fill(nombre)
        self.elements.get_desc_tarea().fill(desc)
        self.agregar_etiquetas()
        self.agregar_prioridad()
        self.agregar_fecha()
        self.elements.get_ver_proyecto()
        self.elements.get_submit_button().click()
        logger.info("se añadio tarea, bandeja de entrada")
        self.verificar_msj()
        
    def agregar_tarea_en_proyecto(self, nombre:str, desc:str):
        self.elements.get_add_tarea_button().click()
        logger.info("abrir form agregar tarea, introducir datos")
        self.elements.get_nombre_tarea().fill(nombre)
        self.elements.get_desc_tarea().fill(desc)
        self.agregar_etiquetas()
        self.agregar_prioridad()
        self.agregar_fecha()
        self.agregar_a()
        self.elements.get_submit_button().click()
        self.verificar_msj()
        logger.info("tarea añadida a proyecto")
        self.eliminar()
    
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
        self.page.screenshot(path='utils/img/actualizar_fecha_tarea.png')
        logger.info("tarea actualizada")
        
    
    def eliminar(self):
        logger.info("eliminar tarea")#eliminar desde bandeja de entrada
        self.page.goto("https://app.todoist.com/app/inbox")
        self.elements.get_abrir_menu_tarea().click()
        self.elements.get_eliminar_tarea().click()
        self.elements.get_msj_alerta_eliminar_tarea()
        self.page.screenshot(path='utils/img/eliminar_tarea.png')
        self.elements.get_eliminar_tarea_button().click()
        logger.info("tarea eliminada")

    def agregar_subtarea(self, nombre_subtarea:str):
        logger.info("agregar sub tarea")
        self.elements.get_select_tarea().click()
        self.elements.get_add_subtarea().click()
        self.elements.get_nombre_tarea_n1().fill(nombre_subtarea)
        self.elements.get_submit_button().click()
        self.elements.get_cancelar_agregar_tarea().click()
        logger.info("sub tarea añadida")
        self.elements.get_cerrar_tarea().click()
    
    def agregar_tarea_nivel2(self, nombre, desc, nombre_subtarea, nombre_subtarea_n2:str):
        self.agregar_tarea_bandeja(nombre, desc)
        self.agregar_subtarea(nombre_subtarea)
        logger.info("agregar tarea en una sub tarea")
        self.elements.get_select_tarea().click()
        logger.info("select sub tarea")
        self.elements.get_select_subtarea().click()
        self.elements.get_add_subtarea().click()
        self.elements.get_nombre_tarea_n1().fill(nombre_subtarea_n2)
        self.elements.get_submit_button().click()
        logger.info("tarea añadida")
        self.elements.get_cerrar_tarea().click()
        
    def agregar_tareas_niveles(self,nombre,desc, niveles):
        logger.info("agregar subtareas hasta 4 niveles de la tarea")
        self.agregar_tarea_bandeja(nombre,desc)
        
        for nivel in range(1, niveles + 1):
            if nivel==1:
                self.elements.get_select_tarea().click() #seleccionar tarea
                self.elements.get_add_subtarea().click() #añadir subtarea n1
                subtarea = f"Subtarea nivel {nivel}"
                self.elements.get_nombre_tarea_n1().fill(subtarea)
                self.elements.get_submit_button().click()
                self.elements.get_cancelar_agregar_tarea().is_visible()
                self.elements.get_cancelar_agregar_tarea().click()
                logger.info(f"Subtarea nivel {nivel} agregada.")
            else:
                self.elements.get_select_subtarea().click()  # seleccionar subtarea
                self.elements.get_add_subtarea().click()
                subtarea = f"Subtarea nivel {nivel}"
                self.elements.get_nombre_tarea_n1().fill(subtarea)
                self.elements.get_submit_button().click()
                # self.page.wait_for_timeout(500)
                self.elements.get_cancelar_agregar_tarea().is_visible()
                self.elements.get_cancelar_agregar_tarea().click()
                
                if nivel==5:
                    logger.info("retrocediendo un nivel")
                    self.elements.get_retroceder_nivel_subtarea().click()
                        # self.page.wait_for_timeout(200)
                    self.page.wait_for_selector(f'text={subtarea}')
                    logger.info("se encontro subtarea")
                    self.page.screenshot(path='utils/img/error_subtarea_nivel.png')
                    raise Exception(f"Subtarea nivel {nivel} se creo en un nivel anterior")
            # Verificación de la subtarea creada
            try:
                self.elements.get_select_subtarea()
                self.page.wait_for_timeout(500)
                self.page.wait_for_selector(f'text={subtarea}', timeout=200)
                logger.info(f"Subtarea nivel {nivel} agregada")

            except:
                # raise Exception(f"Error: la subtarea {nivel} no se creó correctamente.")
                logger.error(f"Error: la subtarea {nivel} no se creó correctamente")

                
    
    def mover_subtarea_a_seccion(self, nombre, desc, nombre_subtarea_n2):
        logger.info("mover subtarea nivel 2 a seccion En proceso")
        self.agregar_tarea_bandeja(nombre,desc)
        self.elements.get_select_tarea().click()
        self.elements.get_add_subtarea().click()
        self.elements.get_nombre_tarea_n1().fill(nombre_subtarea_n2)
        self.elements.get_submit_button().click()
        self.page.wait_for_timeout(500)
        self.elements.get_select_subtarea().click()
        self.elements.get_abrir_menu_tarea().click()
        self.elements.get_mover_tarea().click()
        self.elements.get_selec_seccion_proy().click()
        self.elements.get_msj_alerta_mover_tarea()
        self.page.screenshot(path='utils/img/mover_subtarea.png')
        self.page.wait_for_timeout(1000)
        logger.info("la subtarea se movio a seccion como tarea")
    