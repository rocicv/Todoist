import pytest
from core.webdriver import WebDriver
from main.ui.login.login_page import LoginPage
from main.ui.tareas.page import TaskPage
from dotenv import load_dotenv
import os

load_dotenv()
# Recuperar las variables de entorno
TODOIST_EMAIL = os.getenv("TODOIST_EMAIL")
TODOIST_PASSWORD = os.getenv("TODOIST_PASSWORD")
#variables globales
nombre= "tarea de prueba"
desc = "aquí viene la descripción"


@pytest.fixture
def setup_browser():
    driver = WebDriver()
    driver.start_browser('https://app.todoist.com/auth/login')
    login_page = LoginPage(driver.page)
    login_page.ingresar_valores(TODOIST_EMAIL, TODOIST_PASSWORD)
    login_page.wait_for_dashboard()
    yield driver
    driver.close_browser()

def test_crear_tarea_en_bandeja_entrada(setup_browser):
    driver = setup_browser
    # Usar el Page Object para interactuar con la página de tareas
    proyect_page = TaskPage(driver.page)
    proyect_page.agregar_tarea_bandeja(nombre, desc)

#T-002:Crear una tarea con fecha de vencimiento
def test_crear_tarea_con_fecha_venci(setup_browser):
    driver = setup_browser
    # Usar el Page Object para interactuar con la página de tareas
    proyect_page = TaskPage(driver.page)
    proyect_page.agregar_tarea_con_fvenc(nombre, desc)

# T-003: Crear una tarea en un proyecto
def test_crear_tarea_en_proyecto(setup_browser):
    driver = setup_browser
    # Usar el Page Object para interactuar con la página de tareas
    proyect_page = TaskPage(driver.page)
    proyect_page.agregar_tarea_en_proyecto(nombre, desc)