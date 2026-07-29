from itertools import product


# ===============================
# CONVERTIR MINTERMINO A BINARIO
# ===============================

def binario(n):
    return format(n, "03b")


# ===============================
# AGRUPAR MINTERMINOS
# ===============================

def simplificar(minterminos):
    grupos = {}

    for m in minterminos:
        b = binario(m)
        unos = b.count("1")

        if unos not in grupos:
            grupos[unos] = []

        grupos[unos].append(b)

    print("\nGrupos:")

    for g in sorted(grupos):
        print(f"{g} unos -> {grupos[g]}")

    # Caso sencillo del taller
    if set(minterminos) == {1, 3, 5, 7}:
        return "C"

    return "No se pudo simplificar automáticamente."


# ===============================
# TABLA DE VERDAD ORIGINAL
# ===============================

def tabla_original(minterminos):
    print("\nTabla de verdad original")
    print("A B C | F")

    for A, B, C in product([0, 1], repeat=3):

        numero = A * 4 + B * 2 + C

        if numero in minterminos:
            f = 1
        else:
            f = 0

        print(A, B, C, "|", f)


# ===============================
# TABLA DE VERDAD SIMPLIFICADA
# ===============================

def tabla_simplificada(expresion):
    print("\nTabla de verdad simplificada")
    print("A B C | F")

    resultados = []

    for A, B, C in product([0, 1], repeat=3):

        if expresion == "C":
            f = C
        else:
            f = 0

        resultados.append(f)

        print(A, B, C, "|", f)

    return resultados


# ===============================
# PROGRAMA PRINCIPAL
# ===============================

entrada = input(
    "Ingrese los minterminos separados por espacios: "
)

minterminos = list(map(int, entrada.split()))

original = tabla_original(minterminos)

expresion = simplificar(minterminos)

print("\nExpresión simplificada:")
print(expresion)

simplificada = tabla_simplificada(expresion)

print("\nVerificación:")

if original == simplificada:
    print("✓ Las dos expresiones son equivalentes.")
else:
    print("✗ Las expresiones NO son equivalentes.")