import random
import string

class GeneradorDatos:
    def generar_comentario(self):
        texto = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        comentario = f"{texto}"
        return comentario