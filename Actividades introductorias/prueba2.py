import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Definir niveles de dificultad
def mostrar_palabra(palabra, dificultad):
    if dificultad == "fácil":
        # Mostrar todas las vocales
        for letra in palabra:
            if letra in "aeiou":
                print(letra, end=" ")
            else:
                print("_", end=" ")
    elif dificultad == "media":
        # Mostrar la primer y la última letra
        print(palabra[0], end=" ")
        for _ in range(len(palabra) - 2):
            print("_", end=" ")
        print(palabra[-1], end=" ")
    else:
        # No mostrar ninguna letra
        for _ in palabra:
            print("_", end=" ")

# Número máximo de fallos permitidos
max_fails = 5

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# Pedir nivel de dificultad al usuario
dificultad = input("Selecciona un nivel de dificultad (fácil, medio, difícil): ").lower()

# Mostrar la palabra parcialmente adivinada según el nivel de dificultad
print("Palabra:", end=" ")
mostrar_palabra(secret_word, dificultad)
print()

# Juego principal
fails = 0
while fails < max_fails:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        fails += 1

    # Mostrar la palabra parcialmente adivinada
    print("Palabra:", end=" ")
    mostrar_palabra(secret_word, dificultad)
    print()

    # Verificar si se ha adivinado la palabra completa
    if all(letter in guessed_letters for letter in secret_word):
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has alcanzado el máximo número de fallos ({max_fails}).")
    print(f"La palabra secreta era: {secret_word}")

