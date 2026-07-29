from itertools import product


# ==========================
# EXPRESIONES BOOLEANAS
# ==========================

def expresion1(A, B, C, D):
    return (A and B) or (not C)


def expresion2(A, B, C, D):
    return (A != B) and C      # XOR


def expresion3(A, B, C, D):
    return (A or B) and ((not A) or C)


# ==========================
# TABLA DE VERDAD
# ==========================

def imprimir_tabla(funcion, nombre):
    print("\n" + "=" * 45)
    print(nombre)
    print("=" * 45)
    print("A B C D | Resultado")

    for A, B, C, D in product([0, 1], repeat=4):
        resultado = funcion(bool(A), bool(B), bool(C), bool(D))
        print(f"{A} {B} {C} {D} |     {int(resultado)}")


# Mostrar las tablas de verdad
imprimir_tabla(expresion1, "(A AND B) OR (NOT C)")
imprimir_tabla(expresion2, "(A XOR B) AND C")
imprimir_tabla(expresion3, "(A OR B) AND (NOT A OR C)")


# ==========================
# EVALUAR UNA ENTRADA
# ==========================

print("\nEvaluación de una expresión")

while True:
    opcion = input(
        "\nSeleccione la expresión (1, 2 o 3): "
    )

    if opcion in ("1", "2", "3"):
        break

    print("Opción inválida.")


def leer_valor(variable):
    while True:
        valor = input(f"{variable} (0 o 1): ")

        if valor in ("0", "1"):
            return bool(int(valor))

        print("Ingrese únicamente 0 o 1.")


A = leer_valor("A")
B = leer_valor("B")
C = leer_valor("C")
D = leer_valor("D")


if opcion == "1":
    resultado = expresion1(A, B, C, D)

elif opcion == "2":
    resultado = expresion2(A, B, C, D)

else:
    resultado = expresion3(A, B, C, D)


print("\nResultado:", int(resultado))