from itertools import product


# ==========================================================
# PASO 1: convertir un mintérmino a su representación binaria
# ==========================================================

def a_binario(m, n):
    """Convierte el número m a una cadena binaria de n bits (n = variables)."""
    return format(m, f"0{n}b")


# ==========================================================
# PASO 2: combinar dos términos que difieren en un solo bit
# ==========================================================

def combinar(t1, t2):
    """
    Si t1 y t2 difieren en exactamente una posición, los combina
    reemplazando esa posición por '-' (variable ausente).
    Si difieren en 0 o más de 1 posición, no se pueden combinar.
    """
    diferencias = 0
    resultado = []

    for a, b in zip(t1, t2):
        if a != b:
            diferencias += 1
            if diferencias > 1:
                return None
            resultado.append("-")
        else:
            resultado.append(a)

    return "".join(resultado) if diferencias == 1 else None


# ==========================================================
# PASO 3: generar todos los primos implicantes (Quine-McCluskey)
# ==========================================================

def generar_primos_implicantes(minterminos, n):
    """
    Agrupa y combina términos repetidamente, tal como pide el enunciado
    ("agrupación" / "versión pequeña de Quine-McCluskey").

    Devuelve un diccionario {patron_binario: conjunto_de_minterminos_que_cubre}
    con únicamente los términos que ya NO se pudieron seguir combinando
    (los primos implicantes).
    """
    nivel_actual = {a_binario(m, n): frozenset({m}) for m in minterminos}
    primos = {}

    while nivel_actual:
        terminos = list(nivel_actual.keys())
        combinados = set()
        siguiente_nivel = {}

        # Intentar combinar cada par de términos del nivel actual
        for i in range(len(terminos)):
            for j in range(i + 1, len(terminos)):
                nuevo = combinar(terminos[i], terminos[j])
                if nuevo is not None:
                    combinados.add(terminos[i])
                    combinados.add(terminos[j])
                    cubiertos_previos = siguiente_nivel.get(nuevo, frozenset())
                    siguiente_nivel[nuevo] = (
                        cubiertos_previos
                        | nivel_actual[terminos[i]]
                        | nivel_actual[terminos[j]]
                    )

        # Los términos que no se combinaron con nadie son primos implicantes
        for t in terminos:
            if t not in combinados:
                primos[t] = nivel_actual[t]

        nivel_actual = siguiente_nivel

    return primos


# ==========================================================
# PASO 4: elegir los primos implicantes que cubren todos los
#         minterminos (esenciales primero, luego voraz)
# ==========================================================

def seleccionar_terminos(primos, minterminos):
    """
    Selecciona un subconjunto de primos implicantes que cubra todos
    los minterminos originales:
      1) los primos implicantes esenciales (los únicos que cubren
         cierto mintérmino) se toman siempre;
      2) lo que falte por cubrir se resuelve con una elección voraz
         (se toma en cada paso el primo implicante que cubre más
         minterminos aún no cubiertos).
    """
    cobertura = {m: [] for m in minterminos}
    for termino, cubiertos in primos.items():
        for m in cubiertos:
            if m in cobertura:
                cobertura[m].append(termino)

    seleccionados = set()
    cubiertos_total = set()

    # Primos implicantes esenciales
    for m, lista in cobertura.items():
        if len(lista) == 1:
            seleccionados.add(lista[0])

    for termino in seleccionados:
        cubiertos_total |= primos[termino]

    # Cobertura voraz de lo que falte
    faltantes = set(minterminos) - cubiertos_total
    while faltantes:
        mejor = max(primos, key=lambda t: len(primos[t] & faltantes))
        seleccionados.add(mejor)
        cubiertos_total |= primos[mejor]
        faltantes -= primos[mejor]

    return seleccionados


# ==========================================================
# PASO 5: convertir un patrón binario en texto ("A ∧ ¬C", etc.)
# ==========================================================

def termino_a_texto(termino, variables):
    partes = []

    for letra, bit in zip(variables, termino):
        if bit == "1":
            partes.append(letra)
        elif bit == "0":
            partes.append(f"¬{letra}")
        # bit == '-' -> la variable no aparece en este término

    return " ∧ ".join(partes) if partes else "1"


def expresion_a_texto(terminos, variables):
    if not terminos:
        return "0"
    return " ∨ ".join(termino_a_texto(t, variables) for t in sorted(terminos))


# ==========================================================
# Evaluación de la expresión simplificada (para construir su
# propia tabla de verdad y poder compararla con la original)
# ==========================================================

def evaluar_termino(termino, valores):
    for bit, valor in zip(termino, valores):
        if bit == "1" and valor != 1:
            return False
        if bit == "0" and valor != 0:
            return False
    return True  # bit == '-' no impone condición


def evaluar_expresion(terminos, valores):
    return int(any(evaluar_termino(t, valores) for t in terminos))


# ==========================================================
# TABLA DE VERDAD ORIGINAL  (ahora SÍ retorna la lista de resultados;
# antes esta función solo imprimía y no tenía "return", por eso la
# verificación de equivalencia siempre fallaba)
# ==========================================================

def tabla_original(minterminos, n, variables):
    print("\nTabla de verdad original")
    print(" ".join(variables) + " | F")

    resultados = []

    for combinacion in product([0, 1], repeat=n):
        numero = int("".join(map(str, combinacion)), 2)
        f = 1 if numero in minterminos else 0
        resultados.append(f)
        print(" ".join(map(str, combinacion)), "|", f)

    return resultados


# ==========================================================
# TABLA DE VERDAD SIMPLIFICADA (evalúa la expresión de verdad,
# ya no solo el caso especial "C")
# ==========================================================

def tabla_simplificada(terminos, n, variables):
    print("\nTabla de verdad simplificada")
    print(" ".join(variables) + " | F")

    resultados = []

    for combinacion in product([0, 1], repeat=n):
        f = evaluar_expresion(terminos, combinacion)
        resultados.append(f)
        print(" ".join(map(str, combinacion)), "|", f)

    return resultados


# ==========================================================
# SIMPLIFICAR: junta todo el proceso de Quine-McCluskey
# ==========================================================

def simplificar(minterminos, n, variables):
    primos = generar_primos_implicantes(minterminos, n)
    seleccionados = seleccionar_terminos(primos, minterminos)

    print("\nPrimos implicantes seleccionados:")
    for t in sorted(seleccionados):
        print(f"  {t}  ->  cubre minterminos {sorted(primos[t])}")

    return seleccionados


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def main():
    while True:
        n = input("¿La función tiene 3 o 4 variables?: ").strip()
        if n in ("3", "4"):
            n = int(n)
            break
        print("Ingrese únicamente 3 o 4.")

    variables = ["A", "B", "C", "D"][:n]

    entrada = input("Ingrese los minterminos separados por espacios: ")
    minterminos = list(map(int, entrada.split()))

    original = tabla_original(minterminos, n, variables)

    terminos = simplificar(minterminos, n, variables)
    expresion_texto = expresion_a_texto(terminos, variables)

    print("\nExpresión simplificada (suma de productos):")
    print(expresion_texto)

    simplificada = tabla_simplificada(terminos, n, variables)

    print("\nVerificación:")
    if original == simplificada:
        print("✓ Las dos expresiones son equivalentes.")
    else:
        print("✗ Las expresiones NO son equivalentes.")


if __name__ == "__main__":
    main()