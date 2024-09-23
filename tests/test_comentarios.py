import pytest
from core.webdriver import WebDriver
from main.ui.login.login_page import LoginPage
from main.ui.tareas.page import TaskPage
from main.ui.comentarios.page import CommentPage
from dotenv import load_dotenv
import os

load_dotenv()
# Recuperar las variables de entorno
TODOIST_EMAIL = os.getenv("TODOIST_EMAIL")
TODOIST_PASSWORD = os.getenv("TODOIST_PASSWORD")
#variables globales
nombre= "tarea de prueba"
desc = "aquí viene la descripción de la tarea"
comentario= "Comentario de prueba"

@pytest.fixture
def setup_browser():
    driver = WebDriver()
    driver.start_browser('https://app.todoist.com/auth/login')
    login_page = LoginPage(driver.page)
    login_page.ingresar_valores(TODOIST_EMAIL, TODOIST_PASSWORD)
    login_page.wait_for_dashboard()
    yield driver
    driver.close_browser()

#  C-002: Añadir un comentario a un proyecto
def test_añadir_un_comentario_proyecto(setup_browser):
    driver = setup_browser
    # Usar el Page Object para interactuar con la página de tareas
    coment_page = CommentPage(driver.page)
    coment_page.agregar_coment_a_proy(comentario)


# C-002: Añadir un comentario a una tarea de bandeja de entrada
def test_añadir_un_comentario_tarea(setup_browser):
    driver = setup_browser
    # Usar el Page Object para interactuar con la página de tareas
    coment_page = CommentPage(driver.page)
    task_page = TaskPage(driver.page)
    # task_page.agregar_tarea_bandeja(nombre, desc)
    coment_page.agregar_coment_a_tarea(comentario)

def test_eliminar_comentario_de_tarea(setup_browser):
    driver = setup_browser
    coment_page = CommentPage(driver.page)
    coment_page.eliminar_comentario()

# C-004: Modificar un comentario


# C-005: Reaccionar a un comentario



