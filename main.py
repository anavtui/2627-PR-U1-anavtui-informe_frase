def preparar_texto(frase: str) -> tuple[str, int, int, str]:
    """
    Leer la frase y elimina los espacios de los extremos y convierte el texto a minúsculas. Devuelve el texto preparado.
    recibe el texto preparado y devuelve una tupla con tres datos: número de caracteres —incluidos los espacios interiores—, número de palabras y si contiene la palabra completa "python". Para obtener las palabras, utiliza split().
    :param: frase
    :return: frase_minuscula
    :return: contador_palabras
    :return: contador_caracteres
    :return: python
    """
    frase_minuscula = frase.strip().lower()
    palabras = frase_minuscula.split()
    contador_palabras = len(frase.split())
    contador_caracteres = 0
    python = False

    for caracter in frase:
        contador_caracteres += 1

    if "python" in palabras:
        python = True

    return frase_minuscula, contador_palabras, contador_caracteres, python

def main():

    frase_entrada = input("Entrada: ")
    salida = preparar_texto(frase_entrada)
    print("Salida:")
    print("Texto: ", salida[0])
    print("Caracteres: ", salida[2])
    print("Palabras: ", salida[1])
    if salida[3] == True:
        python = "Sí"
    else:
        python = "No"
    print("Contiene la palabra python: ", python)

if __name__ == "__main__":
    main()