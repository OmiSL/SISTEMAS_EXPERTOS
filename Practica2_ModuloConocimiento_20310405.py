"""
SISTEMAS EXPERTOS
Actividad 2 - P1
    Reconocimiento Facial

Omar Sánchez Larios

notas:
    - 
"""

# Base de conocimiento inicial
base_conocimiento = {
    "Hola": "¡Hola! Estoy aquí para ayudarte. ¿Cómo estás?",
    "¿Cómo estás?": "Estoy bien, gracias por preguntar. ¿En qué puedo ayudarte?",
    "ETC...": "¿De qué te gustaría hablar? Puedo responder preguntas sobre varios temas."
}

def chat():
    while True:
        entrada_usuario = input("Usuario: ").strip().capitalize()
        if entrada_usuario in base_conocimiento:
            respuesta = base_conocimiento[entrada_usuario]
            print("Asistente:", respuesta)
        else:
            print("Asistente: Lo siento, no sé cómo responder a eso.")
            nueva_pregunta = input("Asistente: ¿Qué debería haber respondido? ").strip()
            base_conocimiento[entrada_usuario] = nueva_pregunta
            print("Asistente: Gracias por la información. He aprendido algo nuevo.")

if __name__ == "__main__":
    print("Asistente: Hola, ¿en qué puedo ayudarte hoy?")
    chat()