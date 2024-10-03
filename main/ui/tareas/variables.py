import random
import string

class GeneradorDatos:
    def generar_nombre_tarea(self):
        texto = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        nombre = f"{texto}"
        return nombre
    def generar_descripcion_tarea(self):
        texto = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        desc = f"{texto}"
        return desc