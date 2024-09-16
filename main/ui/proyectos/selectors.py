class ProyectosPageSelectors:
    TITULO_ESPACIO_TRABAJO = "text=Mis Proyectos"
    PROYECTOS_BUTTON = 'div:nth-of-type(1)>button[aria-label="Menú Mis Proyectos"]'
    MENU_POPUP = '[aria-label="Añadir proyecto"]'#pestaña de menu popup
    TITULO_FORMULARIO = "text=Añadir proyecto" 
    CAMPO_NOMBRE = '#edit_project_modal_field_name'
    SELECT_COLOR = 'button[aria-labelledby="edit_project_modal_field_color_label"]'
    VER_COLOR = '#dropdown-select-2-option-charcoal' #color por defecto
    COLOR = 'text=Violeta'
    SUBMIT_BUTTON = 'button[type="submit"]'
    CONTENEDOR_PROYECTO = '[data-testid="task-selection-list-container"]'
    EXPLORAR_PLANTILLAS = 'a[aria-label="Explorar plantillas"]'
    PLANTILLA = 'a[data-template-name="Revisión semanal"]'
    TITULO_PLANTILLA = 'section > div > div > h1'
    COPIAR_PLANTILLA = 'button[data-template-name="Revisión semanal"]'
    