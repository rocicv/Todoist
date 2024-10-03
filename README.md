# Todoist
<p>Proyecto que realiza pruebas web automatizadas sobre la ui de Todoist, se toman en cuenta los modulos de proyectos, comentarios, tareas. Se maneja una estructura de capas, en las que se organizan las pruebas.</p>

1. Clonar repositorio git

```bash
git clone git@github.com:rocicv/Todoist.git
```
2. crear entorno virtual y activar entorno
```bash
python -m venv venv
venv\Scripts\activate
```
3. instalar playright
```bash
pip install pytest playwright
playwright install
```
4. instalar librerias dotenv
```bash
pip install python-dotenv
```
5. Instalar librerias de reportes
```bash
pip install pytest-html
```
6. Añadir dependencias
```bash
pip freeze > requirements.txt
```
## Estructura del proyecto

- `test/`: Contiene las pruebas automatizadas para Todoist.
- `core/`: Contiene archivos esenciales del proyecto.
- `main/`: Carpeta donde se encuentran los scripts principales, page object, selectors, etc.
- `utils/`: Carpeta donde se encuentran las imagenes y reportes de las pruebas


  