# Todoist
1. Clonar repositorio
2. crear entorno virtual y activar
python -m venv venv
venv\Scripts\activate

3. instalar playright
pip install pytest playwright
playwright install

4. instalar librerias dotenv
pip install python-dotenv

5. Añadir dependencias
pip freeze > requirements.txt

6. Agregar archivos de prueba

test/test_ejemplo.py
main/ui/modulo/selectors.py
main/ui/modulo/elements.py
main/ui/modulo/page.py
main/ui/modulo/variables.py

7. Instalar librerias de reportes 
$ pip install pytest-html