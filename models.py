class Persona:
    def __init__(self, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, identificador):
        self._nombre = nombre
        self._primer_apellido = primer_apellido
        self._segundo_apellido = segundo_apellido
        self._fecha_nacimiento = fecha_nacimiento
        self._identificador = identificador

        def definir_puntuacion(self):
            return self


class Villano(Persona):
    def __init__(self, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, identificador):
        super().__init__(nombre, primer_apellido, segundo_apellido, fecha_nacimiento, identificador)
        self.chagepeteador = range(0, 100)
        self.entregador_tardio = range(0, 100)
        self.ausencias = range(0, 100)
        self.hablador = range(0, 100)


class Heroe(Persona):
    def __init__(self, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, identificador):
        super().__init__(nombre, primer_apellido, segundo_apellido, fecha_nacimiento, identificador)
        self.codigo_limpio = range(0, 100)
        self.bien_documentado = range(0, 100)
        self.git_god = range(0, 100)
        self.arquitecto = range(0, 100)
        self.detallista = range(0, 100)

