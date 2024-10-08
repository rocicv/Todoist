import pytest
from core.webdriver import WebDriver
from main.ui.login.login_page import LoginPage
from main.ui.tareas.page import TaskPage
from main.ui.comentarios.page import CommentPage
from main.ui.proyectos.page import ProyectPage
from main.ui.tareas.page import TaskPage
from main.ui.comentarios.variables import GeneradorDatosComentarios
from main.ui.proyectos.variables import GeneradorDatos
from main.ui.tareas.variables import GeneradorDatosTareas

from dotenv import load_dotenv
import os

load_dotenv()
# Recuperar las variables de entorno
TODOIST_EMAIL = os.getenv("TODOIST_EMAIL")
TODOIST_PASSWORD = os.getenv("TODOIST_PASSWORD")
#variables globales
generador = GeneradorDatosComentarios()
comentario = generador.generar_comentario()

generador = GeneradorDatos()
titulo_proyecto = generador.generar_titulo()
correo_generado = generador.generar_correo()

generador = GeneradorDatosTareas()
nombre = generador.generar_nombre_tarea()
desc = generador.generar_descripcion_tarea()

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
    proyect_page = ProyectPage(driver.page)
    coment_page = CommentPage(driver.page)
    proyect_page.agregar_proyecto(titulo_proyecto)
    coment_page.agregar_coment_a_proy(comentario)
    coment_page.eliminar_comentario_proyecto()
    proyect_page.eliminar()


# C-002: Añadir un comentario a una tarea de bandeja de entrada
def test_añadir_un_comentario_tarea(setup_browser):
    driver = setup_browser
    coment_page = CommentPage(driver.page)
    task_page = TaskPage(driver.page)
    task_page.agregar_tarea_bandeja(nombre, desc)
    coment_page.agregar_coment_a_tarea(comentario)
    coment_page.eliminar_comentario()
    task_page.eliminar()



# C-003: Actualizar un comentario
def test_actualizar_comentario(setup_browser):
    driver = setup_browser
    coment_page = CommentPage(driver.page)
    task_page = TaskPage(driver.page)
    task_page.agregar_tarea_bandeja(nombre, desc)
    coment_page.agregar_coment_a_tarea(comentario)
    coment_page.actualizar_info(comentario)
    coment_page.eliminar_comentario()
    task_page.eliminar()


# C-004: Añadir un comentario a una sub tarea
def test_comentario_subtarea(setup_browser):
    driver = setup_browser
    coment_page = CommentPage(driver.page)
    task_page = TaskPage(driver.page)
    task_page.agregar_tarea_bandeja(nombre, desc)
    task_page.agregar_subtarea(1)
    coment_page.comment_subtarea(comentario)
    coment_page.eliminar_comentario()
    task_page.eliminar()



# C-005: Notificar comentario desde proyecto a un correo 
def test_agregar_coment_proyecto_compartido(setup_browser):
    driver = setup_browser
    coment_page = CommentPage(driver.page)
    proyect_page = ProyectPage(driver.page)
    proyect_page.agregar_proyecto(titulo_proyecto)
    proyect_page.compartir_proyecto(correo_generado)
    coment_page.notificar_coment_proy(comentario)
    coment_page.eliminar_comentario_proyecto()
    proyect_page.eliminar() #revisar esto

@pytest.mark.webtest
# C-006: Notificar comentario de tarea a correo
def test_agregar_coment_tarea_pcompartido(setup_browser):
    driver = setup_browser
    coment_page = CommentPage(driver.page)
    proyect_page = ProyectPage(driver.page)
    proyect_page.agregar_proyecto(titulo_proyecto)
    proyect_page.compartir_proyecto(correo_generado)
    task_page = TaskPage(driver.page)
    task_page.agregar_tarea_desde_proyecto(nombre, desc)
    coment_page.notificar_coment_tarea(comentario)
    coment_page.eliminar_comentario()
    task_page.eliminar()
    proyect_page.eliminar()


# C-007: Reaccionar a un comentario
def test_reaccionar_comentario(setup_browser):
    driver = setup_browser
    emoji='corazon'
    coment_page = CommentPage(driver.page)
    coment_page.reaccionar(emoji)
    coment_page.eliminar_comentario()
    coment_page.agregar_coment_a_tarea(comentario)

@pytest.mark.xfail
# C-008: Eliminación de emojis repetidos
def test_se_elimina_reaccion_comentario(setup_browser):
    driver = setup_browser
    coment_page = CommentPage(driver.page)
    emoji='corazon'
    coment_page.reaccionar(emoji)
    coment_page.reaccionar_segundavez()
    # coment_page.eliminar_comentario()
@pytest.mark.xfail
# C-009: Desfase de emojis a un comentario
def test_desfase_reaccion_comentario(setup_browser):
    driver = setup_browser
    task_page = TaskPage(driver.page)
    coment_page = CommentPage(driver.page)
    coment_page.desfasar()
    coment_page.eliminar_comentario()
    task_page.agregar_tarea_bandeja(nombre, desc)