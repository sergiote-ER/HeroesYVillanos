from datetime import datetime
import random
from random import randint


class Persona:
    def __init__(self, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, identificador):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.identificador = identificador

    def calcular_edad(self):
        try:
            f_limpia = self.fecha_nacimiento.strip()
            nacimiento = datetime.strptime(f_limpia, "%d-%m-%Y")
            hoy = datetime.now()
            edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
            return edad
        except Exception:
            return "Fecha invalida"

    def definir_puntuacion(self):
        pass


class Villano(Persona):
    def __init__(self, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, identificador):
        super().__init__(nombre, primer_apellido, segundo_apellido, fecha_nacimiento, identificador)
        self.chagepeteador = random.randint(0, 100)
        self.entregador_tardio = random.randint(0, 100)
        self.ausencias = random.randint(0, 100)
        self.hablador = random.randint(0, 100)
        self.puntuacion_total = self.definir_puntuacion()

    def definir_puntuacion(self):
        return round(
            (self.chagepeteador + self.entregador_tardio + self.ausencias + self.hablador) / 4, 2)


class Heroe(Persona):
    def __init__(self, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, identificador):
        super().__init__(nombre, primer_apellido, segundo_apellido, fecha_nacimiento, identificador)
        self.codigo_limpio = randint(0, 100)
        self.bien_documentado = randint(0, 100)
        self.git_god = randint(0, 100)
        self.arquitecto = randint(0, 100)
        self.detallista = randint(0, 100)
        self.puntuacion_total = self.definir_puntuacion()


    def definir_puntuacion(self):
        return round(
            (self.codigo_limpio + self.bien_documentado + self.git_god + self.arquitecto + self.detallista) / 5, 2)
