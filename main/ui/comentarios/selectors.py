class ComentariosPageSelectors:
    PROYECTO_BUTTON = '#projects_list div[data-testid="virtuoso-item-list"]>div:nth-child(1)' #rescata el primer proyecto 
    COMENTARIO_BUTTON = 'a[data-note-type="project_note"]'
    TEXTO_COMENT_PROY = 'text=Centraliza las discusiones importantes de tu proyecto en los comentarios de proyecto.'
    CAMPO_COMENTARIO = 'p[data-placeholder="Comentar"]'
    SUBMIT_BUTTON = 'button[type="submit"]'
    COMENTARIOS_PROYECTO = '.note_content' #comentarios de proyecto

    ABRIR_TAREA = '.task_list_item >div.task_list_item__body' #seleccionar tarea de today
    ABRIR_CAMPO_COMENTARIO= 'button[data-testid="open-comment-editor-button"]'
    CERRAR_TAREA= '[aria-label="Cerrar tarea"]'
    VER_TAREA = '[data-testid="task-card"]'
    ABRIR_TAREA_INBOX= 'button[aria-label="Abrir detalles de tarea"]'
    SELECT_COMENTARIO = '.note_text has_avatar'
    MENU_COMENTARIO = 'button[aria-label="Opciones del comentario"]'
    ELIMINAR_COMENTARIO_BUTTON = 'div[data-destructive="true"]'
    MENSAJE_ALERTA = 'Este comentario se eliminará permanentemente.'
    ACEPTAR_BUTTON = 'footer > div > button._7ea1378e'

    ACCTIONS_TAREA_BUTTON = '.board_task__details__actions'
    ELIMINAR_TAREA= 'text=¿Eliminar la tarea?'


