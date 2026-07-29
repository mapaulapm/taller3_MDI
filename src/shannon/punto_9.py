from collections import Counter
from math import log2


def calcular_entropia(texto):

    frecuencia = Counter(texto)

    total = len(texto)

    entropia = 0

    print("\nFrecuencias y probabilidades")
    print("-" * 35)

    for simbolo, cantidad in frecuencia.items():

        probabilidad = cantidad / total

        entropia -= probabilidad * log2(probabilidad)

        if simbolo == " ":
            nombre = "' ' (espacio)"
        else:
            nombre = simbolo

        print(
            f"{nombre:12} "
            f"Frecuencia: {cantidad:3} "
            f"Probabilidad: {probabilidad:.4f}"
        )

    return entropia


texto1 = input("Ingrese el primer texto: ")
texto2 = input("Ingrese el segundo texto: ")

print("\n========== TEXTO 1 ==========")
h1 = calcular_entropia(texto1)

print(f"\nEntropía = {h1:.4f} bits")

print("\n========== TEXTO 2 ==========")
h2 = calcular_entropia(texto2)

print(f"\nEntropía = {h2:.4f} bits")

print("\n========== COMPARACIÓN ==========")

if h1 > h2:
    print("El primer texto tiene mayor entropía.")
    print("Contiene una distribución de símbolos más variada.")

elif h2 > h1:
    print("El segundo texto tiene mayor entropía.")
    print("Contiene una distribución de símbolos más variada.")

else:
    print("Ambos textos tienen la misma entropía.")