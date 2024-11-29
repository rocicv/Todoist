# main/selectors.py

class LoginPageSelectors:
    EMAIL_INPUT = 'input[placeholder="Introduce tu email..."]'
    PASSWORD_INPUT = 'input[placeholder="Introduce tu contraseña..."]'
    SUBMIT_BUTTON = 'button[type="submit"]'
    DASHBOARD_URL = "https://app.todoist.com/app/today"
    MSJ_ERROR = "text=Email o contraseña incorrectos."
    MENU_CONFIGURACION = 'button[aria-label="Configuración"]'
    CERRAR_SESION_BUTTON = "text=Cerrar sesión"