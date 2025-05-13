import string
import os

# Define los alfabetos para inglés y español
ALPHABET_EN = string.ascii_lowercase
ALPHABET_ES = 'abcdefghijklmnñopqrstuvwxyz'

def cesar_cipher(text, shift, language='en', decrypt=False):
    """
    Aplica el cifrado César a un texto dado con un desplazamiento especificado.
    Parámetros:
        text (str): El mensaje de entrada.
        shift (int): El número de posiciones a desplazar.
        language (str): 'en' para inglés, 'es' para español.
        decrypt (bool): True para descifrar, False para cifrar.
    Retorna:
        str: El texto cifrado o descifrado.
    """
    if language == 'en':
        alphabet = ALPHABET_EN
    elif language == 'es':
        alphabet = ALPHABET_ES
    else:
        raise ValueError("Idioma no soportado. Use 'en' o 'es'.")

    shift = -shift if decrypt else shift
    result = ''

    for char in text:
        lower_char = char.lower()
        if lower_char in alphabet:
            index = alphabet.index(lower_char)
            new_index = (index + shift) % len(alphabet)
            new_char = alphabet[new_index]
            # Mantiene las mayúsculas
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
        else:
            result += char

    return result

def save_or_display(result_text):
    """
    Permite al usuario guardar el resultado en un archivo o mostrarlo en pantalla.
    """
    print("\n¿Qué deseas hacer con el resultado?")
    print("1. Guardar en un archivo .txt")
    print("2. Mostrar en pantalla")
    choice = input("Elige una opción (1 o 2): ")

    if choice == '1':
        filename = input("Ingresa el nombre del archivo (sin extensión): ") + '.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(result_text)
        print(f"Resultado guardado en '{filename}'")
    elif choice == '2':
        print("\nResultado:")
        print(result_text)
    else:
        print("Opción inválida. Mostrando resultado en pantalla por defecto:")
        print(result_text)

def main():
    print("Bienvenido al aplicativo de Cifrado César\n")

    # Solicita al usuario el texto
    text = input("Ingresa el mensaje que deseas cifrar o descifrar (mínimo 2 líneas):\n")

    # Verifica que haya al menos dos líneas
    # if text.count('\n') < 1:
    #     print("\nError: El mensaje debe tener al menos 2 líneas de texto.")
    #    return

    # Solicita la operación
    print("\n¿Qué deseas hacer?")
    print("1. Cifrar")
    print("2. Descifrar")
    operation = input("Elige una opción (1 o 2): ")
    decrypt = operation == '2'

    # Elige el desplazamiento
    shift = int(input("\nIngresa el nivel de desplazamiento (por ejemplo, 3 o 7): "))

    # Elige el idioma
    print("\nSelecciona el idioma del mensaje:")
    print("1. Español")
    print("2. Inglés")
    lang_choice = input("Elige una opción (1 o 2): ")
    language = 'es' if lang_choice == '1' else 'en'

    # Procesa el mensaje
    result_text = cesar_cipher(text, shift, language=language, decrypt=decrypt)

    # Muestra o guarda el resultado
    save_or_display(result_text)

# Ejecuta la aplicación si es el archivo principal
if __name__ == '__main__':
    main()
