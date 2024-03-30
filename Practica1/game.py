import random
# Lista de palabras posibles
words = ["python", "programacion", "computadora", "código", "desarrollo", "inteligencia"]

# Funcion para mostrar palabra en pantalla
def show_word (word, difficulty):
    if difficulty == "facil":
        # Mostrar todas las vocales de la palabra secreta
        vowels = ['a', 'e', 'i', 'o', 'u']
        word_displayed = ""
        for letter in secret_word:
            if letter in vowels:
                word_displayed += letter
            else:
                word_displayed += "_"
        return word_displayed
    elif difficulty == "media":
        return word[0] + "-" * (len(word) - 2) + word[len(word) - 1]   # muestro la primer y ultima letra de la palabra
    elif difficulty == "dificil":
        return "-" * len (word)      # no muestro ninguna letra de la palabra

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de fallos permitidos (numero de fallos permitidos = tamaño de la palabra secreta)
max_failures = len (secret_word)

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")

#Pedir al jugador que seleccione la dificultad del juego
print ("Seleccione la dificultad del juego: ")
difficulty = input ("Facil / Media / Dificil:  ")

print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# Llamo a la funcion para mostrar la palabra en pantalla segun la dificultad
word_displayed = show_word (secret_word, difficulty)

# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

# inicializo la cantidad de fallos en 0
failures = 0

if difficulty == "facil":
    guessed_letters = ['a', 'e', 'i', 'o', 'u']

if difficulty == "media":
    guessed_letters.append (secret_word[0])
    guessed_letters.append (secret_word[-1])

while failures < max_failures:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word and letter != "":
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        failures = failures + 1
        print (f"Llevas {failures} fallos de {max_failures} permitidos !")

    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")

    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_failures} fallos permitidos.")
    print(f"La palabra secreta era: {secret_word}")

# Nota: Por cada funcionalidad agregada se debe realizar al menos un commit que identifique
# el cambio.
   