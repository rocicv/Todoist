import pytest
from core.webdriver import WebDriver
from main.ui.login.login_page import LoginPage
from main.ui.proyectos.page import ProyectPage
from main.ui.proyectos.variables import GeneradorDatos
from dotenv import load_dotenv
import os

load_dotenv()
# Recuperar las variables de entorno
TODOIST_EMAIL = os.getenv("TODOIST_EMAIL")
TODOIST_PASSWORD = os.getenv("TODOIST_PASSWORD")
#Datos generados
generador = GeneradorDatos()
correo_generado = generador.generar_correo()
titulo_proyecto = generador.generar_titulo()
desc_plantilla = generador.generar_desc_plantilla()

@pytest.fixture
def setup_browser():
    driver = WebDriver()
    driver.start_browser('https://app.todoist.com/auth/login')
    login_page = LoginPage(driver.page)
    login_page.ingresar_valores(TODOIST_EMAIL, TODOIST_PASSWORD)
    login_page.wait_for_dashboard()
    yield driver
    driver.close_browser()


# P-001: Agregar un proyecto simple
def test_agregar_proyecto_simple(setup_browser):
    driver = setup_browser
    # Usar el Page Object para interactuar con la página de proyecto
    proyect_page = ProyectPage(driver.page)
    proyect_page.agregar_proyecto(titulo_proyecto)
    proyect_page.eliminar()

# P-002: Agregar proyecto por plantilla
def test_agregar_proyecto_por_plantilla(setup_browser):
    driver = setup_browser
   
    proyect_page = ProyectPage(driver.page)
    proyect_page.agregar_proyecto_plantilla()
    proyect_page.eliminar()

@pytest.mark.webtest
# P-003: Agregar secciones en un proyecto 
def test_agregar_secciones_en_proyecto(setup_browser):
    driver = setup_browser
    
    proyect_page = ProyectPage(driver.page)
    proyect_page.agregar_proyecto(titulo_proyecto)
    proyect_page.agregar_seccion()
    proyect_page.eliminar()


# P-004: Agregar un proyecto como una plantilla
def test_agregar_proyecto_como_plantilla(setup_browser):
    driver = setup_browser
   
    proyect_page = ProyectPage(driver.page)
    proyect_page.agregar_proyecto(titulo_proyecto)
    proyect_page.agregar_seccion()
    proyect_page.crear_platilla(desc_plantilla)
    proyect_page.eliminar()


# P-005: Agregar proyecto simple a favoritos
def test_agregar_p_simple_a_favoritos(setup_browser):
    driver = setup_browser
   
    proyect_page = ProyectPage(driver.page)
    proyect_page.agregar_proyecto(titulo_proyecto)
    proyect_page.añadir_a_favorito()
    proyect_page.eliminar()

# P-006: Actualizar información de proyecto simple
def test_actualizar_info_proyecto(setup_browser):
    driver = setup_browser
   
    proyect_page = ProyectPage(driver.page)
    proyect_page.agregar_proyecto(titulo_proyecto)
    proyect_page.actualizar_info()
    proyect_page.eliminar()


# P-007: Compartir proyecto por correo
def test_compartir_proyecto(setup_browser):
    driver = setup_browser
   
    proyect_page = ProyectPage(driver.page)
    proyect_page.agregar_proyecto(titulo_proyecto)
    proyect_page.compartir_proyecto(correo_generado)
    proyect_page.eliminar()


# P-008: Archivar un proyecto 
def test_archivar_proyecto(setup_browser):
    driver = setup_browser
  
    proyect_page = ProyectPage(driver.page)
    proyect_page.agregar_proyecto(titulo_proyecto)
    proyect_page.archivar()
    

# P-009: Eliminar un proyecto
def test_eliminar_proyecto(setup_browser):
    driver = setup_browser
    
    proyect_page = ProyectPage(driver.page)
    proyect_page.agregar_proyecto(titulo_proyecto)
    proyect_page.eliminar()

# P-010: Exportar proyecto en cvs
def test_exportar_proyecto(setup_browser):
    driver = setup_browser
    
    proyect_page = ProyectPage(driver.page)
    proyect_page.agregar_proyecto_plantilla()
    proyect_page.exportar()
    proyect_page.eliminar()