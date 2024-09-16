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

6. Agregar archivos te prueba

test/test_ejemplo.py
main/ui/carpeta/selectors.py
main/ui/carpeta/elements.py
main/ui/carpeta/page.py