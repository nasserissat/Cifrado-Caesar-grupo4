# Mensaje original (mínimo dos líneas)
mensaje = """El conocimiento protege la informacion.
La criptografia es la ciencia de secretos."""

def caesar(texto: str, shift: int) -> str:
    """
    Cifra (o descifra, si el desplazamiento es negativo) usando César.
    Mantiene mayúsculas, minúsculas y deja intactos espacios, acentos y signos.
    """
    resultado = []
    for ch in texto:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            offset = (ord(ch) - base + shift) % 26
            resultado.append(chr(base + offset))
        else:
            resultado.append(ch)
    return "".join(resultado)

# Generar y mostrar los dos cifrados
for k in (3, 7):
    cifrado = caesar(mensaje, k)
    print(f"\n--- Desplazamiento +{k} ---")
    print(cifrado)

    # Ejemplo de descifrado (aplicando el desplazamiento inverso)
    print("\nDescifrado de prueba:")
    print(caesar(cifrado, -k))