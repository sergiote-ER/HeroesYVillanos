from log import Log
from factoria import FactoriaPersonaje
import random


def main():
    log = Log()
    fabrica = FactoriaPersonaje()
    registro_personajes = []

    # Bloque try-except para la inicialización de los personajes de prueba (añadido el identificador que faltaba)
    try:
        registro_personajes.append(
            fabrica.crear_personaje("heroe", "Francisco", "Escobar", "López", "19-01-1968", "H001"))
        registro_personajes.append(
            fabrica.crear_personaje("villano", "Paulo", "Tovar", "De Godoy", "12-08-1976", "V001"))
        log.escribir("INFO", "Sistema iniciado con personajes de prueba.")
    except Exception as e:
        log.escribir("ERROR", f"Error al inicializar personajes de prueba: {e}")

    while True:
        print("\n================ MENÚ HÉROES Y VILLANOS ================")
        print("1. Crear nuevo personaje")
        print("2. Listar todos los personajes")
        print("3. Buscar personajes por atributo o cualidad")
        print("4. Emparejar Héroe y Villano aleatoriamente")
        print("5. Ver edad de los personajes")
        print("6. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            print("\n--- CREAR PERSONAJE ---")
            tipo = input("¿Es 'heroe' o 'villano'?: ").strip().lower()
            if tipo not in ["heroe", "villano"]:
                print("Error: Tipo incorrecto. Debe ser 'heroe' o 'villano'.")
                log.escribir("WARNING", "Intento fallido de creación por tipo incorrecto.")
                continue

            nombre = input("Nombre: ")
            p_apellido = input("Primer apellido: ")
            s_apellido = input("Segundo apellido: ")
            f_nac = input("Fecha de nacimiento (DD-MM-YYYY): ")

            try:
                if tipo == "heroe":
                    prefijo = "H"
                else:
                    prefijo = "V"

                contador_tipo = 0
                for p in registro_personajes:
                    if p["tipo"].lower() == tipo:
                        contador_tipo = contador_tipo + 1

                numero = contador_tipo + 1
                iden = f"{prefijo}{numero:03d}"  # Ejemplo: H001, H002, V001, V002...

                nuevo = fabrica.crear_personaje(tipo, nombre, p_apellido, s_apellido, f_nac, iden)
                registro_personajes.append(nuevo)

                print(
                    f"¡{tipo.capitalize()} creado con exito! ID asignado: {iden} | Puntuacion total: {nuevo['puntuacion_total']}")
                log.escribir("INFO", f"Creado {tipo} con identificador automatico {iden}.")

            except Exception as e:
                print(f"Se ha producido un error al crear el personaje: {e}")
                log.escribir("ERROR", f"Error en creación de personaje: {e}")

        elif opcion == "2":
            if not registro_personajes:
                print("\n[Aviso] No hay ningun personaje creado todavía en el sistema.")
                log.escribir("WARNING", "Intento de listar personajes con la base de datos vacía.")
            else:
                for p in registro_personajes:
                    print(
                        f"\n[{p['tipo']}] ID: {p['identificador']} - Nombre: {p['nombre']} {p['primer_apellido']} - Puntuacion Total: {p['puntuacion_total']}")

        elif opcion == "3":
            print("\n--- BUSQUEDA ---")
            if not registro_personajes:
                print("\n[Aviso] No se puede realizar ninguna busqueda porque no hay personajes creados.")
                log.escribir("WARNING", "Intento de busqueda con la base de datos vacia.")
                continue

            atributo = input(
                "Introduce el atributo o cualidad a buscar (ej: nombre, identificador, git_god, chagepeteador): ").strip().lower()
            valor = input("Introduce el valor a buscar: ").strip()

            try:
                encontrados = []
                for p in registro_personajes:
                    if atributo in p:
                        val_personaje = str(p[atributo])
                        if valor.lower() in val_personaje.lower():
                            encontrados.append(p)

                if encontrados:
                    print(f"\nSe han encontrado {len(encontrados)} coincidencia(s):")
                    for p in encontrados:
                        print(f"- [{p['tipo']}] {p['nombre']} {p['primer_apellido']} ({atributo}: {p.get(atributo)})")
                    log.escribir("INFO", f"Busqueda exitosa por {atributo} = {valor}.")
                else:
                    print("No se han encontrado personajes con ese criterio.")
            except Exception as e:
                print(f"Ocurrio un error durante la busqueda: {e}")
                log.escribir("ERROR", f"Error en busqueda por {atributo}: {e}")


        elif opcion == "4":
            try:
                if not registro_personajes:
                    print("\n[Aviso] No hay personajes en el sistema para realizar un emparejamiento.")
                    log.escribir("WARNING", "Intento de emparejamiento con la base de datos vacía.")
                    continue

                heroes = []
                for p in registro_personajes:
                    if p["tipo"] == "Heroe":
                        heroes.append(p)

                villanos = []
                for p in registro_personajes:
                    if p["tipo"] == "Villano":
                        villanos.append(p)

                if not heroes or not villanos:
                    print("Se necesita al menos 1 héroe y 1 villano para hacer un emparejamiento.")
                else:
                    h = random.choice(heroes)
                    v = random.choice(villanos)
                    diferencia = abs(h["puntuacion_total"] - v["puntuacion_total"])

                    print(f"\n--- ENFRENTAMIENTO ---")
                    print(
                        f"Héroe: {h['nombre']} ({h['puntuacion_total']} pts) vs Villano: {v['nombre']} ({v['puntuacion_total']} pts)")

                    if diferencia <= 15:
                        print("⚖️ Estado: ¡Combate muy igualado! (Diferencia menor o igual a 15 pts)")
                    else:
                        print("⚡ Estado: Combate desequilibrado (Hay mucha diferencia de nivel)")

                    if h["puntuacion_total"] > v["puntuacion_total"]:
                        print(f"Resultado: ¡Gana el Heroe {h['nombre']} con {h['puntuacion_total']} puntos!")
                        log.escribir("INFO",
                                     f"Enfrentamiento: Victoria para el heroe {h['nombre']} frente a {v['nombre']}.")

                    elif v["puntuacion_total"] > h["puntuacion_total"]:
                        print(f"Resultado: ¡Gana el Villano {v['nombre']} con {v['puntuacion_total']} puntos!")
                        log.escribir("INFO",
                                     f"Enfrentamiento: Victoria para el villano {v['nombre']} frente a {h['nombre']}.")

                    else:
                        print("Resultado: ¡Empate tecnico! Ambos tienen exactamente la misma puntuación.")
                        log.escribir("INFO", f"Enfrentamiento: Empate entre {h['nombre']} y {v['nombre']}.")

            except Exception as e:
                print(f"Error al realizar el emparejamiento: {e}")
                log.escribir("ERROR", f"Error en emparejamiento: {e}")

        elif opcion == "5":
            print("\n--- EDAD DE LOS PERSONAJES ---")
            if not registro_personajes:
                print("\n[Aviso] No hay personajes registrados para consultar sus edades.")
                log.escribir("WARNING", "Intento de consulta de edades con la base de datos vacía.")
            else:
                for p in registro_personajes:
                    print(
                        f"- [{p['tipo']}] {p['nombre']} {p['primer_apellido']} (ID: {p['identificador']}) -> Edad: {p['edad']} años (Nacimiento: {p['fecha_nacimiento']})")
                log.escribir("INFO", "Consulta de edades de los personajes realizada.")

        elif opcion == "6":
            print("Saliendo del programa.")
            log.escribir("INFO", "Cierre del programa.")
            break
        else:
            print("Opción no válida. Introduce un número del 1 al 6.")


if __name__ == "__main__":
    main()
