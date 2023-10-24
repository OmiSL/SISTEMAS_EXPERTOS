"""
    Omar Sánchez Larios
    20310405
    
    Sistemas Expertos
    
    Práctica 2:
        Adivina quien
"""

""" --------------------------------------------------- TABLE ---------------------------------------------------------- """

from tabulate import tabulate

# Inicializa la lista de animales
frutas = [
    {"nombre": "Manzana", "es_dulce": True, "color": "rojo", "es_citrica": False},
    {"nombre": "Naranja", "es_dulce": False, "color": "naranja", "es_citrica": True},
    {"nombre": "Banana", "es_dulce": True, "color": "amarillo", "es_citrica": False},
    {"nombre": "Limón", "es_dulce": False, "color": "verde", "es_citrica": True},
    {"nombre": "Fresa", "es_dulce": True, "color": "rojo", "es_citrica": False},
]

# Agrega atributos adicionales
for fruta in frutas:
    fruta["es_grande"] = False
    fruta["tiene_semillas"] = False

""" -------------------------------------------------- FUNCTIONS ---------------------------------------------------------- """
    
def mostrar_frutas(frutas):
    if not frutas:
        print("No hay frutas en la lista.")
        return

    atributos = list(frutas[0].keys())
    headers = atributos.copy()

    tabla = []
    for fruta in frutas:
        fila = [fruta[atributo] for atributo in atributos]
        tabla.append(fila)

    print("\nTabla de Frutas:")
    print(tabulate(tabla, headers, tablefmt="grid"))


def adivinar_fruta(frutas):
    print("Piensa en una fruta y responde las siguientes preguntas con 's' o 'n'.")
    atributos = list(frutas[0].keys())

    for atributo in atributos[1:]:  # Comienza desde el segundo atributo
        if hacer_pregunta(f"¿La fruta es {atributo}?"):
            frutas = [f for f in frutas if f[atributo]]
        else:
            frutas = [f for f in frutas if not f[atributo]]

    if len(frutas) == 0:
        print("No encontré ninguna fruta con esos atributos.")
        print("Gracias por jugar.")
    elif len(frutas) == 1:
        respuesta_correcta = hacer_pregunta(f"¿Tu fruta es una {frutas[0]['nombre']}? (s/n)")
        if respuesta_correcta:
            print("¡He adivinado correctamente!")
        else:
            print(f"No he adivinado correctamente. Tu fruta no es una {frutas[0]['nombre']}.")
            if hacer_pregunta("¿Quieres agregar una nueva fruta?"):
                agregar_nueva_fruta()
                if hacer_pregunta("¿Quieres agregar un nuevo atributo?"):
                    nuevo_atributo = input("Nombre del nuevo atributo a agregar a cada fruta: ")
                    agregar_atributo_individual(nuevo_atributo)
            else:
                print("¡Hasta luego!")
    else:
        print("No pude adivinar la fruta. ¡Has ganado!")
        
        
def hacer_pregunta(pregunta):
    respuesta = input(pregunta + " (s/n): ").strip().lower()
    while respuesta not in ["s", "n"]:
        print("Por favor, responde con 's' o 'n'.")
        respuesta = input(pregunta + " (s/n): ").strip().lower()
    return respuesta == "s"


def agregar_nueva_fruta():
    nueva_fruta = {}
    nueva_fruta["nombre"] = input("Nombre de la nueva fruta: ")

    for atributo in frutas[0].keys():
        if atributo != "nombre":
            respuesta = input(f"¿La fruta '{nueva_fruta['nombre']}' es '{atributo}'? (s/n): ").strip().lower()
            nueva_fruta[atributo] = respuesta == "s"

    frutas.append(nueva_fruta)
    print(f"Se ha agregado a {nueva_fruta['nombre']} a la base de datos.")
    
    
def agregar_atributo_individual(atributo):
    for fruta in frutas:
        respuesta = input(f"¿La fruta '{fruta['nombre']}' es '{atributo}'? (s/n): ").strip().lower()
        if respuesta == "s":
            fruta[atributo] = True
        elif respuesta == "n":
            fruta[atributo] = False
        else:
            print("Respuesta no válida. Por favor, responde con 's' o 'n'.")


def jugar_de_nuevo():
    respuesta = hacer_pregunta("¿Quieres jugar de nuevo?")
    return respuesta


""" ----------------------------------------------------------- MAIN ---------------------------------------------------------- """

while True:
    mostrar_frutas(frutas)
    adivinar_fruta(frutas)
    if not jugar_de_nuevo():
        if hacer_pregunta("¿Quieres agregar una nueva fruta?"):
            agregar_nueva_fruta()
            if hacer_pregunta("¿Quieres agregar un nuevo atributo?"):
                nuevo_atributo = input("Nombre del nuevo atributo a agregar a cada fruta: ")
                agregar_atributo_individual(nuevo_atributo)
        else:
            print("¡Gracias por jugar! Hasta luego!")
            break