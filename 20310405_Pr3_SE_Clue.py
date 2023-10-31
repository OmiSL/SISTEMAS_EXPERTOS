"""
    Omar Sanchez Larios
    20310405
    
    Sistemas Expertos
    
    Practica 3:
        CLUE
"""

import random
""" --------------------------------------------------- TABLE ---------------------------------------------------------- """

personajes = ["Luke Skywalker", "Han Solo", "Darth Vader", "Yoda", "Obi-Wan Kenobi"]
armas = ["Sable de luz", "Bláster", "Ballesta Wookiee", "Pistola DL-44", "Fusil E-11"]
lugares = ["Tatooine", "Endor", "Hoth", "Dagobah", "Alderaan"]

# Copias de las listas de personajes, armas y habitaciones
personajes_disponibles = list(personajes)
armas_disponibles = list(armas)
lugares_disponibles = list(lugares)

""" -------------------------------------------------- FUNCTIONS ---------------------------------------------------------- """

def obtener_escenario_sin_repeticiones(personajes, armas, lugares):
    if not personajes:
        personajes = list(personajes_disponibles)
    if not armas:
        armas = list(armas_disponibles)
    if not lugares:
        lugares = list(lugares_disponibles)

    personaje = random.choice(personajes)
    arma = random.choice(armas)
    lugar = random.choice(lugares)
    personajes.remove(personaje)
    armas.remove(arma)
    lugares.remove(lugar)
    return personaje, arma, lugar

escenarios = []
for i in range(5):
    personaje, arma, lugar = obtener_escenario_sin_repeticiones(personajes, armas, lugares)
    escenarios.append((personaje, arma, lugar))

escenario_culpable = None
while escenario_culpable is None or escenario_culpable in escenarios:
    escenario_culpable = obtener_escenario_sin_repeticiones(personajes, armas, lugares)

# Crear un diccionario para llevar un registro de las consultas realizadas
consultas_realizadas = {"personaje": [], "arma": [], "lugar": []}

def generar_pistas(escenarios, escenario_culpable, consultas_realizadas):
    pistas = []
    for escenario in escenarios:
        personaje, arma, habitacion = escenario
        pista = f"{personaje} dijo haber estado en {habitacion} y ver {arma}"
        pistas.append(pista)

    pistas_lugares = [f"{lugar} es un lugar importante en la historia." for lugar in lugares]
    pistas.extend(pistas_lugares)

    return pistas

pistas = generar_pistas(escenarios, escenario_culpable, consultas_realizadas)

def mostrar_pistas_seleccionadas(opcion, seleccion, escenario_culpable):
    pistas_mostradas = []

    for pista in pistas:
        if opcion in pista.lower() and seleccion in pista:
            pistas_mostradas.append(pista)

    registro_personaje = escenario_culpable[0]
    registro_lugar = escenario_culpable[2]
    registro_arma = escenario_culpable[1]

    mensaje = []

    for pista in pistas_mostradas:
        elementos = pista.split()
        personaje_en_pista = elementos[0]
        lugar_en_pista = elementos[5]
        arma_en_pista = elementos[-1]

        registro_personaje_text = "No" if personaje_en_pista == registro_personaje else "Sí"
        registro_lugar_text = "No" if lugar_en_pista == registro_lugar else "Sí"
        registro_arma_text = "No" if arma_en_pista == registro_arma else "Sí"

        mensaje.append(f"Hay registros del {personaje_en_pista}: {registro_personaje_text}")
        mensaje.append(f"Hay registros de la {lugar_en_pista}: {registro_lugar_text}")
        mensaje.append(f"Hay registros del {arma_en_pista}: {registro_arma_text}")

    return pistas_mostradas, mensaje

""" ----------------------------------------------------------- MAIN ---------------------------------------------------------- """

# Inicio del juego
print("¡Bienvenido al juego Clue!")

preguntas_restantes = 5  # Número de preguntas permitidas

while preguntas_restantes > 0:
    print(f"\nPreguntas restantes: {preguntas_restantes}")

    opcion = input("¿Qué tipo de pista deseas (personaje, arma, lugar)?: ").strip().lower()
    if opcion not in ["personaje", "arma", "lugar"]:
        print("Opción no válida.")
        continue

    if opcion == "personaje":
        opciones_disponibles = personajes_disponibles
    elif opcion == "arma":
        opciones_disponibles = armas_disponibles
    elif opcion == "lugar":
        opciones_disponibles = lugares_disponibles

    if opciones_disponibles:
        print(f"Opciones disponibles de {opcion}: {', '.join(opciones_disponibles)}")
        seleccion = input(f"Selecciona el {opcion} del cual deseas información: ").strip()

        if seleccion in opciones_disponibles:
            pistas_seleccionadas, registro = mostrar_pistas_seleccionadas(opcion, seleccion, escenario_culpable)
            if pistas_seleccionadas:
                print("Pistas relacionadas:")
                for i, pista in enumerate(pistas_seleccionadas, 1):
                    print(f"Pista {i}: {pista}")
            else:
                print(f"No hay pistas disponibles para {seleccion}.")

            if registro is not None:
                print(registro)

            preguntas_restantes -= 1
            opciones_disponibles.remove(seleccion)
        else:
            print(f"La selección '{seleccion}' no es válida.")
    else:
        print(f"No hay opciones disponibles de {opcion}.")

# Adivinar a los culpables
print("\n¡Ha llegado el momento de adivinar a los culpables!")
personaje_culpable = input("¿Quién crees que es el personaje culpable?: ").strip()
arma_culpable = input("¿Qué arma crees que se utilizó?: ").strip()
lugar_culpable = input("¿En qué habitación crees que ocurrió el crimen?: ").strip()

if (personaje_culpable == escenario_culpable[0] and
    arma_culpable == escenario_culpable[1] and
    lugar_culpable == escenario_culpable[2]):
    print("¡Felicidades! Has adivinado a los culpables y resuelto el misterio. ¡Ganas el juego!")
else:
    print("Lo siento, no has adivinado a los culpables. El juego ha terminado.")
    print(f"Los culpables eran: {escenario_culpable[0]} con {escenario_culpable[1]} en {escenario_culpable[2]}.")
