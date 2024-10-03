# test_login.py

from core.webdriver import WebDriver
from main.ui.login.login_page import LoginPage
from dotenv import load_dotenv
import os


load_dotenv()
# Recuperar las variables de entorno
TODOIST_EMAIL = os.getenv("TODOIST_EMAIL")
TODOIST_PASSWORD = os.getenv("TODOIST_PASSWORD")

def test_login_con_credenciales_validas():
    driver = WebDriver()
    driver.start_browser('https://app.todoist.com/auth/login')
    
    # Usar el Page Object para interactuar con la página de login
    login_page = LoginPage(driver.page)
 
    login_page.ingresar_valores(TODOIST_EMAIL, TODOIST_PASSWORD)
    
    # 3. Verificar que el usuario sea redirigido a la página principal
    login_page.wait_for_dashboard()
    # 4. Cerrar sesion
    login_page.logout()
    # 5. Cerrar el navegador
    driver.close_browser()

def test_login_con_credenciales_no_validas():
    driver = WebDriver()
    driver.start_browser('https://app.todoist.com/auth/login')
    
    # Usar el Page Object para interactuar con la página de login
    login_page = LoginPage(driver.page)
    login_page.page.set_default_timeout(2000)
    # 2. Ingresar las credenciales
    email = "prueba@gmail.com"
    password = "credencialnovalida"
    login_page.ingresar_valores(email, password)
    # 3. Verificar que el usuario sea redirigido a la página principal
    login_page.wait_for_dashboard()
    
    # 4. Cerrar el navegador
    driver.close_browser()