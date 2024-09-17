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
    PROYECTO = 'ul[aria-label="Selecciona un proyecto"]>li:nth-of-type(3)' #Proyecto mis cosas