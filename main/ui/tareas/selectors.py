class TareasPageSelectors:
    ADD_TAREA_BUTTON = 'div.app-sidebar-container > div> nav > div > button'
    NOMBRE_TAREA = '[aria-label="Nombre de la tarea"]'
    DESC_TAREA = '[aria-label="Descripción"]'
    
    ETIQUETA_BUTTON = '[aria-label="Añadir etiquetas"]' #abre el menu etiquetas
    ETIQUETA = '[data-value="etiqueta"]' #seleccionar opcion
    POPPER_OVERLAY  = '.popper__overlay'

    PRIORIDAD_BUTTON = '[aria-label="Establecer prioridad"]'#abre menu prioridad
    PRIORIDAD = '[aria-label="Prioridad 1"]'#selecciona prioridad 1

    DATE_BUTTON= 'div[aria-label="Establecer fecha de vencimiento"]'
    DATE='button[data-action-hint="scheduler-suggestion-tomorrow"]'

    PROYECTO ='button[aria-label="Selecciona un proyecto"]>span>div>span'
    SUBMIT_BUTTON = '[data-testid="task-editor-submit-button"]'
    BANDEJA_ENTRADA_BUTTON = 'a[href="/app/inbox"]'
    MENSAJE_ALERT = '[data-testid="toasts-container"]'

    SELECT_A_BUTTON= 'button[aria-label="Selecciona un proyecto"]'
    MENU_PROYECTOS = 'ul[aria-label="Selecciona un proyecto"]'
    PROYECTO = 'ul[aria-label="Selecciona un proyecto"]>li:nth-of-type(1)' #Proyecto mis cosas

    PROYECTO_L1= '#projects_list > div > div > div > div > div:nth-of-type(1)' #primer proyecto de la lista
    ADD_BUTTON_PROYECT='.section_list > li > section > div > ul > li > button'


    ADD_BUTTON_SECTION='section[aria-label="Pendiente"]  .list_holder button' #boton añadir tarea de seccion pendiente
    MENU_TAREA='[aria-label="Más acciones"]'
    MOVER_TAREA_BUTTON='[aria-label="menú editar tarea"] > div:nth-of-type(7)'
    SECCION_PENDIENTE_PROY='li[aria-label="Sección: En proceso (Proyecto: Mis cosas)"]'
    MENSAJE_ALERT_MOVER_TAREA ="text=Cambiaste el orden"
    
    CANCELAR_BUTTON='button[aria-label="Cancelar"]'
    EDITAR_TAREA_BUTTON='[aria-label="menú editar tarea"] > div:nth-of-type(3)'
    DATE_PROXIMA_SEMANA ='button[data-action-hint="scheduler-suggestion-nextWeek"]'
    
    ELIMINAR_TAREA_BUTTON='[data-action-hint="task-overflow-menu-delete"]'
    MENSAJE_ALERT_ELIMINAR_TAREA='text=¿Eliminar la tarea?'
    BUTON_ELIMINAR='footer > div > button:nth-of-type(2)'