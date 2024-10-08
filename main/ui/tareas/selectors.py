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
    ANADIR_A_BUTTON ='button[aria-label="Selecciona un proyecto"]>span>div>span'
    SUBMIT_BUTTON = '[data-testid="task-editor-submit-button"]'
    BANDEJA_ENTRADA_BUTTON = 'a[href="/app/inbox"]'
    MENSAJE_ALERT = '[data-testid="toasts-container"]'
    SELECT_A_BUTTON= 'button[aria-label="Selecciona un proyecto"]'
    MENU_PROYECTOS = 'ul[aria-label="Selecciona un proyecto"]'
    PROYECTO = '.dropdown_select--popup ul li[role="separator"] + li' #Proyecto mis cosas, sin seccion
    LISTA_PROYECTOS= '#projects_list > div > div > div > div > div:nth-of-type(1)' #primer proyecto de la lista
    ADD_BUTTON_PROYECT='.section_list > li:nth-of-type(1) > section > div > ul > li > button'#boton añadir tarea, sin seccion
    ADD_BUTTON_SECTION='section[aria-label="Pendiente"]  .list_holder button' #boton añadir tarea de seccion pendiente
    MENU_TAREA='button[aria-label="Más acciones"]'
    MENU_TAREA_DENTRO_SECCION='.task_list_item  button[aria-label="Más acciones"]'
    MENU_SUB_TAREA='#task-detail-subtasks-panel button[data-testid="more_menu"]'
    MOVER_TAREA_BUTTON='[aria-label="menú editar tarea"] > div:nth-of-type(7)'
    INBOX='li.dropdown_select__option--highlighted'
    SECCION_PROCESO_PROY='li.dropdown_select__option--highlighted +li +li >div> div:nth-of-type(2)'
    SECCION_PROCESO_INBOX='li.dropdown_select__option--highlighted + li + li'
    MENSAJE_ALERT_MOVER_TAREA ="text=Cambiaste el orden"
    CANCELAR_BUTTON='button[aria-label="Cancelar"]'
    EDITAR_TAREA_BUTTON='[aria-label="menú editar tarea"] > div:nth-of-type(3)'
    DATE_PROXIMA_SEMANA ='button[data-action-hint="scheduler-suggestion-nextWeek"]'
    ELIMINAR_TAREA_BUTTON='[data-action-hint="task-overflow-menu-delete"]'
    MENSAJE_ALERT_ELIMINAR_TAREA='text=¿Eliminar la tarea?'
    BUTON_ELIMINAR='.focus-marker-enabled-within button:nth-of-type(2)'
    TAREA='li.task_list_item>div' #seleccionar tarea de today
    ADD_SUBTAREA='text=Añadir subtarea'
    CERRAR_TAREA_BUTTON='button[aria-label="Cerrar tarea"]'
    NOMBRE_TAREA_N1='form > div.task_editor__editing_area > div> div  div[aria-label="Nombre de la tarea"]'
    SELECT_SUBTAREA='li.task_list_item.task_list_item--project_hidden > div'
    SUBTAREA_BREARCUMB='div[data-testid="task-detail-breadcrumbs"]>a'
    
