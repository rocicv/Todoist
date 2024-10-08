import random
import string

class GeneradorDatos:
    def generar_correo(self):
        dominio = "ejemplo.com"  
        nombre_usuario = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        correo = f"{nombre_usuario}@{dominio}"
        return correo
    def generar_titulo(self):
        titulo = "Proyecto"  
        proyecto = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        titulo_proyecto = f"{titulo} {proyecto}"
        return titulo_proyecto
    
    def generar_desc_plantilla(self): 
        descripcion = ''.join(random.choices(string.ascii_lowercase + string.digits, k=30))
        desc_plantilla = f"{descripcion}"
        return desc_plantilla