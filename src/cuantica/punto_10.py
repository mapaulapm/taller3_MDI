import numpy as np

# ===========================
# COMPUERTAS CUÁNTICAS
# ===========================

X = np.array([
    [0, 1],
    [1, 0]
])

Z = np.array([
    [1, 0],
    [0, -1]
])

H = (1 / np.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
])

# Estado inicial |0>
estado_inicial = np.array([1, 0], dtype=float)


# ===========================
# FUNCIONES
# ===========================

def aplicar_compuerta(estado, compuerta):
    return np.dot(compuerta, estado)


def probabilidades(estado):
    p0 = abs(estado[0])**2
    p1 = abs(estado[1])**2
    return p0, p1


def medir(estado, veces=1000):

    p0, p1 = probabilidades(estado)

    resultados = np.random.choice(
        [0, 1],
        size=veces,
        p=[p0, p1]
    )

    ceros = np.sum(resultados == 0)
    unos = np.sum(resultados == 1)

    print(f"\nProbabilidad de medir 0: {p0:.4f}")
    print(f"Probabilidad de medir 1: {p1:.4f}")

    print(f"\nResultados de {veces} mediciones:")
    print(f"0 -> {ceros}")
    print(f"1 -> {unos}")


# ===========================
# MENÚ
# ===========================

print("Compuertas disponibles")
print("1. X")
print("2. Z")
print("3. H")
print("4. H seguida de H")

opcion = input("\nSeleccione una opción: ")

estado = estado_inicial.copy()

if opcion == "1":
    estado = aplicar_compuerta(estado, X)
    print("\nAplicando X")

elif opcion == "2":
    estado = aplicar_compuerta(estado, Z)
    print("\nAplicando Z")

elif opcion == "3":
    estado = aplicar_compuerta(estado, H)
    print("\nAplicando H")

elif opcion == "4":
    estado = aplicar_compuerta(estado, H)
    estado = aplicar_compuerta(estado, H)
    print("\nAplicando H seguida de H")

else:
    print("Opción inválida.")
    exit()

print("\nEstado final:")
print(estado)

medir(estado)