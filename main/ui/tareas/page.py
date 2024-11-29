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
    def agregar_tarea(self, nombre:str, desc:str):
        logger.info("Introducir datos")
        self.elements.get_nombre_tarea().fill(nombre)
        self.elements.get_desc_tarea().fill(desc)
        self.agregar_etiquetas()
        self.agregar_prioridad()
        
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
        self.page.screenshot(path='utils/img/alerta_aparece.png')# Tomar una captura de pantalla del mensaje


    def agregar_tarea_bandeja(self, nombre:str, desc:str):
        self.elements.get_add_tarea_button().click()
        self.agregar_tarea(nombre, desc)
        #por defecto fecha hoy
        self.elements.get_ver_proyecto()
        self.elements.get_submit_button().click()
        logger.info("se añadio tarea, bandeja de entrada")
        self.verificar_msj()
      
        
    def agregar_tarea_con_fvenc(self, nombre:str, desc:str):
        self.elements.get_add_tarea_button().click()
        logger.info("abrir form agregar tarea, introducir datos")
        self.agregar_tarea(nombre, desc)
        self.agregar_fecha()
        # self.elements.get_ver_proyecto()#bandeja de entrada
        self.elements.get_submit_button().click()
        logger.info("se añadio tarea, bandeja de entrada")
        self.verificar_msj()
        self.page.goto("https://app.todoist.com/app/inbox")
       
        
    def agregar_tarea_en_proyecto(self, nombre:str, desc:str):
        self.page.goto("https://app.todoist.com/app/today")
        self.elements.get_add_tarea_button().click()
        logger.info("abrir form agregar tarea, introducir datos")
        self.agregar_tarea(nombre, desc)
        self.agregar_fecha()
        self.agregar_a()
        self.elements.get_submit_button().click()
        self.verificar_msj()
        logger.info("tarea añadida a proyecto")
        self.elements.get_select_proyecto_1().click()
      
    
    def agregar_tarea_desde_proyecto(self, nombre:str, desc:str):
        self.elements.get_select_proyecto_1().click()
        self.elements.get_add_task_project().click()
        logger.info("abrir form agregar tarea, introducir datos")
        self.agregar_tarea(nombre, desc)
        self.agregar_fecha()
        self.elements.get_submit_button().click()
        self.verificar_msj()
        logger.info("tarea añadida a proyecto")
        self.elements.get_cancelar_agregar_tarea().click()
     
    
    def mover_tarea(self, nombre:str, desc:str):
        logger.info("crear tarea en seccion Pendiente")
        self.elements.get_select_proyecto_1().click()
        self.elements.get_add_task_section().click()
        logger.info("abrir form agregar tarea, introducir datos")
        self.agregar_tarea(nombre, desc)
        self.agregar_fecha()
        self.elements.get_submit_button().click()
        logger.info("tarea añadida a seccion")       
        self.elements.get_cancelar_agregar_tarea().click()
        self.page.hover("li.task_list_item")
        logger.info("abrir menu tarea y mover")
        self.elements.get_abrir_menu_tarea_seccion().click()
        self.elements.get_mover_tarea().click()
        logger.info("elegir seccion")
        self.elements.get_selec_seccion_proy().click()
        self.elements.get_msj_alerta_mover_tarea() #captura imagen
        self.page.screenshot(path='utils/img/mover_tarea.png')
        logger.info("la tarea se movio a seccion En proceso")
        
    
    def actualizar_info(self, nombre, desc):
        self.elements.get_add_tarea_button().click()
        self.agregar_tarea(nombre, desc)
        self.elements.get_ver_proyecto()
        self.elements.get_submit_button().click()
        logger.info("se añadio tarea, bandeja de entrada")
        self.verificar_msj()
        logger.info("actualizar la informacion de tarea")
        self.page.goto("https://app.todoist.com/app/inbox")
        hover_selector = ".board_task"
        self.page.hover(hover_selector)
        self.elements.get_abrir_menu_tarea().click()
        self.elements.get_editar_tarea().click()
        self.elements.get_abrir_fvenc_button().click()
        self.elements.get_selec_nueva_fecha().click()
        self.elements.get_submit_button().click()
        self.page.screenshot(path='utils/img/actualizar_fecha_tarea.png')
        logger.info("tarea actualizada")

    def eliminar(self):
        hover_selector = "li.task_list_item"
        self.page.hover(hover_selector)
        self.elements.get_abrir_menu_tarea().is_visible()
        self.elements.get_abrir_menu_tarea().click()
        self.elements.get_eliminar_tarea().click()
        self.elements.get_msj_alerta_eliminar_tarea()
        self.page.screenshot(path='utils/img/eliminar_tarea.png')
        self.elements.get_eliminar_tarea_button().click()
        self.page.wait_for_timeout(500)
        logger.info("Tarea eliminada")

    def eliminar_inbox(self):
        hover_selector = ".board_task"
        self.page.hover(hover_selector)
        self.elements.get_abrir_menu_tarea().is_visible()
        self.elements.get_abrir_menu_tarea().click()
        self.elements.get_eliminar_tarea().click()
        self.elements.get_msj_alerta_eliminar_tarea()
        self.page.screenshot(path='utils/img/eliminar_tarea.png')
        self.elements.get_eliminar_tarea_button().click()
        self.page.wait_for_timeout(500)
        logger.info("Tarea eliminada")

    def eliminar_tarea_seccion(self):
        hover_selector = "li.task_list_item"
        self.page.hover(hover_selector)
        self.elements.get_abrir_menu_tarea_seccion().is_visible()
        self.elements.get_abrir_menu_tarea_seccion().click()
        self.elements.get_eliminar_tarea().click()
        self.elements.get_msj_alerta_eliminar_tarea()
        self.page.screenshot(path='utils/img/eliminar_tarea.png')
        self.elements.get_eliminar_tarea_button().click()
        self.page.wait_for_timeout(500)
        logger.info("Tarea eliminada")

    def eliminar2(self):
        # Obtener la URL actual
        current_url = self.page.url
        
        # Determinar el selector según la URL obtenida
        if current_url == "https://app.todoist.com/app/inbox":
            hover_selector = ".board_task"
        elif current_url == "https://app.todoist.com/app/today":
            hover_selector = "li.task_list_item"
        elif current_url.startswith("https://app.todoist.com/app/project/"): 
            hover_selector = "li.task_list_item"
        else:
            logger.warning("No se encontró una URL válida para eliminar el registro.")
            return  # Salir si no es una URL válida

        logger.info(f'url {current_url}')
        # para eliminar tarea enviar el hover que es diferente
        self._eliminar_tarea(hover_selector)
    
    def _eliminar_tarea(self, hover_selector):
        #Método auxiliar para eliminar la tarea haciendo hover sobre el 
        logger.info(f'Intentando hacer hover en {hover_selector}')
        try: 
            self.page.hover(hover_selector)
            self.elements.get_abrir_menu_tarea().is_visible()
           
            menu_selector='button[aria-label="Más acciones"]'
            combined_selector = f"{hover_selector} {menu_selector}"
            logger.info(f"{combined_selector}")
            self.page.locator(combined_selector).click()
            self.elements.get_eliminar_tarea().click()
            self.elements.get_msj_alerta_eliminar_tarea()
            self.page.screenshot(path='utils/img/eliminar_tarea.png')
            self.elements.get_eliminar_tarea_button().click()
            self.page.wait_for_timeout(500)
            logger.info("Tarea eliminada")
        except Exception as e:
            logger.warning(f"No se pudo abrir el menú de la tarea: {str(e)}")

    def agregar_subtarea(self, nivel):#revisando este metodo
        logger.info("agregar sub tarea")
        subtarea = f"Subtarea nivel {nivel}"
        self.elements.get_select_tarea().click()
        self.elements.get_add_subtarea().click()
        self.elements.get_nombre_tarea_n1().fill(subtarea)
        self.elements.get_submit_button().click()
        self.elements.get_cancelar_agregar_tarea().click()
        logger.info("sub tarea añadida")
        self.elements.get_cerrar_tarea().click()
    

    def agregar_subtarea_nivel2(self, nivel):
        logger.info("agregar tarea en una sub tarea")
        subtarea = f"Subtarea nivel {nivel}"
        self.elements.get_select_tarea().click()
        logger.info("select sub tarea")
        self.elements.get_select_subtarea().click()
        self.elements.get_add_subtarea().click()
        self.elements.get_nombre_tarea_n1().fill(subtarea)
        self.elements.get_submit_button().click()
        logger.info(f"subtarea 2 añadida")
        self.elements.get_cerrar_tarea().click()
        

    def agregar_tareas_niveles(self, niveles):
        logger.info("agregar subtareas hasta 4 niveles de la tarea")
        
        for nivel in range(1, niveles + 1):
            if nivel==1:
                self.elements.get_select_tarea().click() #seleccionar tarea
                self.elements.get_add_subtarea().click() #añadir subtarea n1
                subtarea = f"Subtarea nivel {nivel}"
                self.elements.get_nombre_tarea_n1().fill(subtarea)
                self.elements.get_submit_button().click()
                self.elements.get_cancelar_agregar_tarea().is_visible()
                self.elements.get_cancelar_agregar_tarea().click()
            else:
                self.elements.get_select_subtarea().click()  # seleccionar subtarea
                self.elements.get_add_subtarea().click()
                subtarea = f"Subtarea nivel {nivel}"
                self.elements.get_nombre_tarea_n1().fill(subtarea)
                self.elements.get_submit_button().click()
                self.elements.get_cancelar_agregar_tarea().is_visible()
                self.elements.get_cancelar_agregar_tarea().click()
                
                if nivel==5:
                    logger.info("retrocediendo un nivel")
                    self.elements.get_retroceder_nivel_subtarea().click()
                    self.page.wait_for_selector(f'text={subtarea}')
                    logger.info(f"se encontro subtarea ")
                    self.page.screenshot(path='utils/img/error_subtarea_nivel.png')
                    self.elements.get_cerrar_tarea().click()
                    self.eliminar()
                    raise Exception(f"Subtarea nivel {nivel} se creo en un nivel anterior")
            # Verificación de la subtarea creada
            try:
                self.elements.get_select_subtarea()
                self.page.wait_for_timeout(500)
                self.page.wait_for_selector(f'text={subtarea}', timeout=200)
                logger.info(f"Subtarea nivel {nivel} agregada")

            except:
                logger.error(f"Error: la subtarea {nivel} no se creó correctamente")

        self.elements.get_cerrar_tarea().click()
                
    
    def mover_subtarea_a_inbox(self):
        logger.info("mover subtarea nivel 2 a inbox")
        self.elements.get_select_tarea().click()
        self.page.hover("li.task_list_item.task_list_item--project_hidden")
        self.elements.get_abrir_menu_sub_tarea().click()
        self.elements.get_mover_tarea().click()
        self.elements.get_selec_inbox().click()
        self.elements.get_msj_alerta_mover_tarea()
        self.page.screenshot(path='utils/img/mover_subtarea.png')
        self.page.wait_for_timeout(1000)
        logger.info("la subtarea se movio a inbox como tarea")
        self.elements.get_cerrar_tarea().click()
        self.eliminar()
        # self.elements.get_select_proyecto_1().click()
        self.page.goto('https://app.todoist.com/app/inbox')
        self.page.wait_for_timeout(500)
        self.page.screenshot(path='utils/img/subtarea_se_movio.png')
        # self.eliminar()
    
    