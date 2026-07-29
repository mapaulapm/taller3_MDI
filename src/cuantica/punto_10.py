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
estado = np.array([1, 0], dtype=float)


# ===========================
# APLICAR COMPUERTA
# ===========================

def aplicar_compuerta(estado, compuerta):
    return np.dot(compuerta, estado)


# ===========================
# PROBABILIDADES
# ===========================

def probabilidades(estado):
    p0 = abs(estado[0]) ** 2
    p1 = abs(estado[1]) ** 2

    print(f"P(0) = {p0:.4f}")
    print(f"P(1) = {p1:.4f}")

    return p0, p1


# ===========================
# MEDICIONES
# ===========================

def medir(estado, veces=1000):

    p0, p1 = probabilidades(estado)

    resultados = np.random.choice(
        [0, 1],
        size=veces,
        p=[p0, p1]
    )

    ceros = np.sum(resultados == 0)
    unos = np.sum(resultados == 1)

    print(f"\nDespués de {veces} mediciones:")
    print(f"0 -> {ceros}")
    print(f"1 -> {unos}")


# ===========================
# PRUEBA 1
# ===========================

print("===== X|0> =====")

estado_x = aplicar_compuerta(estado, X)

print("Estado:", estado_x)

medir(estado_x)


# ===========================
# PRUEBA 2
# ===========================

print("\n===== H|0> =====")

estado_h = aplicar_compuerta(estado, H)

print("Estado:", estado_h)

medir(estado_h)


# ===========================
# PRUEBA 3
# ===========================

print("\n===== HH|0> =====")

estado_hh = aplicar_compuerta(
    aplicar_compuerta(estado, H),
    H
)

print("Estado:", estado_hh)

medir(estado_hh)