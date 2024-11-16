import pytest
from core.webdriver import WebDriver
from main.ui.login.login_page import LoginPage
from main.ui.tareas.page import TaskPage
from main.ui.proyectos.page import ProyectPage
from main.ui.tareas.variables import GeneradorDatosTareas
from main.ui.proyectos.variables import GeneradorDatos
from dotenv import load_dotenv
import os

load_dotenv()
# Recuperar las variables de entorno
TODOIST_EMAIL = os.getenv("TODOIST_EMAIL")
TODOIST_PASSWORD = os.getenv("TODOIST_PASSWORD")
#variables globales
generador = GeneradorDatosTareas()
nombre = generador.generar_nombre_tarea()
desc = generador.generar_descripcion_tarea()
generador = GeneradorDatos()
titulo_proyecto = generador.generar_titulo()

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
    task_page = TaskPage(driver.page)
    task_page.agregar_tarea_bandeja(nombre, desc)
    task_page.eliminar()


# T-002: Crear una tarea en un proyecto
def test_crear_tarea_en_proyecto(setup_browser):
    driver = setup_browser
    #crear_proyecto primero
    proyect_page = ProyectPage(driver.page)
    proyect_page.agregar_proyecto(titulo_proyecto)
    #agregar tarea en proyecto
    task_page = TaskPage(driver.page)
    task_page.agregar_tarea_en_proyecto(nombre, desc)
    task_page.eliminar()
    proyect_page.eliminar()

#T-003:Crear una tarea con fecha de vencimiento del dia siguiente 
def test_crear_tarea_con_fecha_venci(setup_browser):
    driver = setup_browser
    task_page = TaskPage(driver.page)
    task_page.agregar_tarea_con_fvenc(nombre, desc)
    task_page.eliminar_inbox()

# T-004: Crear una tarea desde un proyecto
def test_crear_tarea_desde_proyecto(setup_browser):
    driver = setup_browser
    task_page = TaskPage(driver.page)
    proyect_page = ProyectPage(driver.page)
    proyect_page.agregar_proyecto(titulo_proyecto)
    # proyect_page.agregar_seccion()
    task_page.agregar_tarea_desde_proyecto(nombre, desc)
    task_page.eliminar()
    proyect_page.eliminar()


# T-005: Mover tarea entre secciones
def test_mover_tarea_entre_secciones(setup_browser):
    driver = setup_browser
    task_page = TaskPage(driver.page)
    proyect_page = ProyectPage(driver.page)
    proyect_page.agregar_proyecto(titulo_proyecto)
    proyect_page.agregar_seccion()
    task_page.mover_tarea(nombre, desc)
    task_page.eliminar_tarea_seccion()
    proyect_page.eliminar()


# T-006: Actualizar información de tarea en bandeja en entrada 
def test_actualizar_info_tarea(setup_browser):
    driver = setup_browser
    task_page = TaskPage(driver.page)
    task_page.actualizar_info(nombre, desc)
    task_page.eliminar_inbox()

# @pytest.mark.webtest
# T-007: Añadir sub tarea a tarea 
def test_agregar_subtarea(setup_browser):
    driver = setup_browser
    task_page = TaskPage(driver.page)
    task_page.agregar_tarea_bandeja(nombre, desc)
    task_page.agregar_subtarea(1)
    task_page.eliminar()

# T-008: Añadir una tarea en sub tarea 
def test_agregar_tarea_subtarea(setup_browser):
    driver = setup_browser
    task_page = TaskPage(driver.page)
    task_page.agregar_tarea_bandeja(nombre, desc)
    task_page.agregar_subtarea(1)
    task_page.agregar_subtarea_nivel2(2)
    task_page.eliminar()
@pytest.mark.webtest
# T-009: Añadir 4 niveles de subtarea en una tarea 
def test_agregar_cuatro_niveles_subtarea(setup_browser):
    driver = setup_browser
    task_page = TaskPage(driver.page)
    task_page.agregar_tarea_bandeja(nombre, desc)
    task_page.agregar_tareas_niveles( 4)
    task_page.eliminar()

# T-010: Mover subtarea a  inbox 
def test_mover_subtarea_a_inbox(setup_browser):
    driver = setup_browser
    task_page = TaskPage(driver.page)
    task_page.agregar_tarea_bandeja(nombre, desc)
    task_page.agregar_subtarea(1)
    task_page.mover_subtarea_a_inbox()
    task_page.eliminar_inbox()


@pytest.mark.xfail
#T-011: Se permite crear una subtarea nivel 5 en otro nivel
def test_agregar_subtarea_n5(setup_browser):
    driver = setup_browser
    task_page = TaskPage(driver.page)
    task_page.agregar_tarea_bandeja(nombre, desc)
    task_page.agregar_tareas_niveles(5)
    task_page.eliminar()