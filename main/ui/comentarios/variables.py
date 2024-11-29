import random
import string

class GeneradorDatosComentarios:
    def generar_comentario(self):
        texto = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        comentario = f"{texto}"
        return comentario