import pytest
from core.webdriver import WebDriver
from main.ui.login.login_page import LoginPage
from main.ui.tareas.page import TaskPage
from main.ui.comentarios.page import CommentPage
from main.ui.comentarios.variables import GeneradorDatos
from dotenv import load_dotenv
import os

load_dotenv()
# Recuperar las variables de entorno
TODOIST_EMAIL = os.getenv("TODOIST_EMAIL")
TODOIST_PASSWORD = os.getenv("TODOIST_PASSWORD")
#variables globales
generador = GeneradorDatos()
comentario = generador.generar_comentario()

@pytest.fixture
def setup_browser():
    driver = WebDriver()
    driver.start_browser('https://app.todoist.com/auth/login')
    login_page = LoginPage(driver.page)
    login_page.ingresar_valores(TODOIST_EMAIL, TODOIST_PASSWORD)
    login_page.wait_for_dashboard()
    yield driver
    driver.close_browser()

#  C-001: Añadir un comentario a un proyecto
def test_añadir_un_comentario_proyecto(setup_browser):
    driver = setup_browser
    # Usar el Page Object para interactuar con la página de tareas
    coment_page = CommentPage(driver.page)
    coment_page.agregar_coment_a_proy(comentario)
    #eliminar comentario de proyecto
    coment_page.eliminar_comentario_proyecto()

# C-002: Añadir un comentario a una tarea de bandeja de entrada
def test_añadir_un_comentario_tarea(setup_browser):
    driver = setup_browser
    # Usar el Page Object para interactuar con la página de tareas
    coment_page = CommentPage(driver.page)
    task_page = TaskPage(driver.page)
    # task_page.agregar_tarea_bandeja(nombre, desc)
    coment_page.agregar_coment_a_tarea(comentario)
    coment_page.eliminar_comentario()
# C-003: Eliminar un comentario de una tarea
def test_eliminar_comentario_de_tarea(setup_browser):
    driver = setup_browser
    coment_page = CommentPage(driver.page)
    coment_page.eliminar_comentario()

# C-004: Actualizar un comentario
def test_actualizar_comentario(setup_browser):
    driver = setup_browser
    coment_page = CommentPage(driver.page)
    coment_page.actualizar_info(comentario)
    coment_page.eliminar_comentario()
# C-005: Reaccionar a un comentario de tarea
def test_reaccionar_comentario_tarea(setup_browser):
    driver = setup_browser
    coment_page = CommentPage(driver.page)
    coment_page.reaccionar_comment_tarea()
    coment_page.eliminar_comentario()
# C-006: Añadir un comentario a una sub tarea
def test_comentario_subtarea(setup_browser):
    driver = setup_browser
    coment_page = CommentPage(driver.page)
    coment_page.comment_subtarea(comentario)
    # coment_page.eliminar_comentario()
# C-007: Eliminación de reaccion emojis repetidos
def test_eliminar_emoji_repetido(setup_browser):
    driver = setup_browser
    coment_page = CommentPage(driver.page)
    coment_page.agregar_coment_a_tarea(comentario)
    coment_page.reaccionar_comment_tarea()
    coment_page.reaccionar_comment_tarea()
# C-008: Desfase de emojis a un comentario


