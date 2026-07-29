def ingreso_grafo():

    grafo = {}

    n = int(input("Ingrese el número de materias: "))

    print("\nIngrese el nombre de cada materia:")

    for _ in range(n):
        materia = input("Materia: ").strip().upper()
        grafo[materia] = []

    m = int(input("\nIngrese el número de conflictos: "))

    print("\nIngrese cada conflicto (Materia1 Materia2):")

    for i in range(m):
        print(f"Conflicto {i+1}:")
        a, b = input().split()

        a = a.upper()
        b = b.upper()

        grafo[a].append(b)
        grafo[b].append(a)

    return grafo

def colorear_grafo(grafo):

    colores = {}

    for vertice in grafo:

        usados = set()

        for vecino in grafo[vertice]:

            if vecino in colores:
                usados.add(colores[vecino])

        color = 1

        while color in usados:
            color += 1

        colores[vertice] = color

    return colores
def verificar(grafo, colores):

    for vertice in grafo:

        for vecino in grafo[vertice]:

            if colores[vertice] == colores[vecino]:
                return False

    return True

def mostrar_resultados(colores):

    horarios = {}

    for materia, color in colores.items():

        if color not in horarios:
            horarios[color] = []

        horarios[color].append(materia)

    print("\n===== HORARIOS =====\n")

    for color in sorted(horarios):
        print(f"Horario {color}: {', '.join(horarios[color])}")

    print(f"\nTotal de horarios utilizados: {len(horarios)}")

def main():

    print(" ASIGNACIÓN DE HORARIOS \n")

    grafo = ingreso_grafo()

    colores = colorear_grafo(grafo)

    if verificar(grafo, colores):
        print("\nColoreo válido.")
    else:
        print("\nError: existe un conflicto.")

    mostrar_resultados(colores)


if __name__ == "__main__":
    main()    
