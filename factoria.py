from models import Heroe, Villano


class FactoriaPersonaje:

    def crear_personaje(self, tipo, nombre, primer_apellido, segundo_apellido, fecha_nacimiento, identificador):
        try:
            tipo_lower = tipo.strip().lower()
            if tipo_lower == "heroe":
                personaje = Heroe(nombre, primer_apellido, segundo_apellido, fecha_nacimiento, identificador)
                return {
                    "tipo": "Heroe",
                    "identificador": personaje.identificador,
                    "nombre": personaje.nombre,
                    "apellidos": f"{personaje.primer_apellido} {personaje.segundo_apellido}",
                    "edad": personaje.calcular_edad(),
                    "cualidades": {
                        "codigo_limpio": personaje.codigo_limpio,
                        "bien_documentado": personaje.bien_documentado,
                        "git_god": personaje.git_god,
                        "arquitecto": personaje.arquitecto,
                        "detallista": personaje.detallista
                    },
                    "puntuacion_total": personaje.puntuacion_total
                }
            elif tipo_lower == "villano":
                personaje = Villano(nombre, primer_apellido, segundo_apellido, fecha_nacimiento, identificador)
                return {
                    "tipo": "Villano",
                    "identificador": personaje.identificador,
                    "nombre": personaje.nombre,
                    "apellidos": f"{personaje.primer_apellido} {personaje.segundo_apellido}",
                    "edad": personaje.calcular_edad(),
                    "cualidades": {
                        "chagepeteador": personaje.chagepeteador,
                        "entregador_tardio": personaje.entregador_tardio,
                        "ausencias": personaje.ausencias,
                        "hablador": personaje.hablador
                    },
                    "puntuacion_total": personaje.puntuacion_total
                }
            else:
                raise ValueError(f"Tipo de personaje desconocido: {tipo}")

        except Exception as e:
            raise Exception(f"Error dentro de la factoría al crear el personaje: {e}")
