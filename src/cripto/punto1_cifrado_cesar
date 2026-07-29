abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def desplazar_caracter(caracter, desplazamiento):
    # Si no es una letra que este definida, se devuelve igual
    if caracter.upper() not in abc:
        return caracter
  # Guardamos si originalmente era mayúscula
    es_mayuscula = caracter.isupper()

    # Posición de la letra en el alfabeto
    indice = abc.index(caracter.upper())

    # Nuevo índice aplicando el desplazamiento
    nuevo_indice = (indice + desplazamiento) % 26

    # Nueva letra
    nueva_letra = abc[nuevo_indice]

    # Se respeta el formato original
    if es_mayuscula:
        return nueva_letra
    else:
        return nueva_letra.lower()

def cifrar(texto, desplazamiento):
    resultado = ""

    for caracter in texto:
        resultado += desplazar_caracter(caracter, desplazamiento)

    return resultado
def descifrar(texto, desplazamiento):
    return cifrar(texto, -desplazamiento)
def fuerza_bruta(texto):
    print("\nPosibles descifrados:\n")

    for desplazamiento in range(26):
        posible_texto = descifrar(texto, desplazamiento)
        print(f"k = {desplazamiento:2}: {posible_texto}")

def menu():
    while True:
        print("\n===== CIFRADO CÉSAR =====")
        print("1. Cifrar")
        print("2. Descifrar")
        print("3. Fuerza bruta")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            texto = input("Ingrese el texto: ")
            k = int(input("Ingrese el desplazamiento: "))
            print("\nTexto cifrado:")
            print(cifrar(texto, k))

        elif opcion == "2":
            texto = input("Ingrese el texto cifrado: ")
            k = int(input("Ingrese el desplazamiento: "))
            print("\nTexto descifrado:")
            print(descifrar(texto, k))

        elif opcion == "3":
            texto = input("Ingrese el texto cifrado: ")
            fuerza_bruta(texto)

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()