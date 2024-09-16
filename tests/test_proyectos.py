from core.webdriver import WebDriver
from main.ui.login.login_page import LoginPage
from main.ui.proyectos.page import ProyectPage
from dotenv import load_dotenv
import os

load_dotenv()
# Recuperar las variables de entorno
TODOIST_EMAIL = os.getenv("TODOIST_EMAIL")
TODOIST_PASSWORD = os.getenv("TODOIST_PASSWORD")

def test_agregar_proyecto_simple():
    # prerequisitos
    driver = WebDriver()
    driver.start_browser('https://app.todoist.com/auth/login')
    login_page = LoginPage(driver.page)
    login_page.ingresar_valores(TODOIST_EMAIL, TODOIST_PASSWORD)
    login_page.wait_for_dashboard()
    

    # Usar el Page Object para interactuar con la página de proyecto
    proyect_page = ProyectPage(driver.page)
    titulo = "proyecto de prueba"
    proyect_page.agregar_proyecto(titulo)

    # Cerrar el navegador
    driver.close_browser()

def test_agregar_proyecto_por_plantilla():
     # prerequisitos
    driver = WebDriver()
    driver.start_browser('https://app.todoist.com/auth/login')
    login_page = LoginPage(driver.page)
    login_page.ingresar_valores(TODOIST_EMAIL, TODOIST_PASSWORD)
    login_page.wait_for_dashboard()
    

    # Usar el Page Object para interactuar con la página de proyecto
    proyect_page = ProyectPage(driver.page)
    proyect_page.agregar_proyecto_plantilla()

    # Cerrar el navegador
    driver.close_browser()
