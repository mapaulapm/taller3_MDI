import heapq
from copy import deepcopy

def dijkstra(grafo, origen):
    """
    Calcula la distancia mínima desde el nodo origen a todos los demás nodos.

    Parámetros:
        grafo: diccionario de diccionarios
        origen: nodo inicial

    Retorna:
        distancias: distancia mínima desde el origen
        anteriores: nodo anterior en el camino más corto
    """

    # Inicializar distancias
    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[origen] = 0

    # Para reconstruir caminos
    anteriores = {nodo: None for nodo in grafo}

    # Cola de prioridad (distancia, nodo)
    cola = [(0, origen)]

    while cola:
        distancia_actual, actual = heapq.heappop(cola)

        # Si ya encontramos un camino mejor, ignoramos este
        if distancia_actual > distancias[actual]:
            continue

        # Revisar vecinos
        for vecino, peso in grafo[actual].items():
            nueva_distancia = distancia_actual + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = actual
                heapq.heappush(cola, (nueva_distancia, vecino))

    return distancias, anteriores

def reconstruir_camino(anteriores, origen, destino):
    """
    Reconstruye el camino mínimo desde origen hasta destino.
    """

    camino = []
    actual = destino

    while actual is not None:
        camino.append(actual)
        actual = anteriores[actual]

    camino.reverse()

    if camino[0] == origen:
        return camino

    return []

def ingreso_grafo():
    grafo={}

    n=int(input("Ingrese el número de nodos"))
    print("\nIngrese el nombre de cada nodo:")
    for _ in range(n):
        nodo = input("Nodo: ").strip().upper()
        grafo[nodo] = {}

    a = int(input("\nIngrese el número de aristas: "))

    print("\nIngrese las aristas en el formato:")
    print("origen destino peso")

    for i in range(a):
        print(f"\nArista {i+1}:")
        origen, destino, peso = input().split()

        origen = origen.upper()
        destino = destino.upper()
        peso = float(peso)

        grafo[origen][destino] = peso
        grafo[destino][origen] = peso   # Grafo no dirigido

    return grafo   

def eliminar_nodo(grafo, nodo):
    if nodo not in grafo:
        print("El nodo no existe.")
        return

    # Eliminar el nodo
    grafo.pop(nodo)

    # Eliminar las conexiones hacia ese nodo
    for vecino in grafo:
        if nodo in grafo[vecino]:
            del grafo[vecino][nodo]

def eliminar_arista(grafo, origen, destino):
    if origen in grafo and destino in grafo[origen]:
        del grafo[origen][destino]

    if destino in grafo and origen in grafo[destino]:
        del grafo[destino][origen]

def ingreso_pares(grafo):
    """
    Pide al usuario los pares origen-destino que se quieren analizar
    (mínimo 5, según lo pedido en el enunciado).
    """
    while True:
        cantidad = int(input("\n¿Cuántos pares origen-destino desea probar (mínimo 5)? "))
        if cantidad >= 5:
            break
        print("Debe ingresar al menos 5 pares.")

    pares = []
    print("\nIngrese cada par en el formato: origen destino")
    for i in range(cantidad):
        while True:
            print(f"\nPar {i + 1}:")
            origen, destino = input().split()
            origen, destino = origen.upper(), destino.upper()

            if origen not in grafo or destino not in grafo:
                print("Alguno de los dos nodos no existe en el grafo. Intente de nuevo.")
                continue
            pares.append((origen, destino))
            break

    return pares


def calcular_distancias_pares(grafo, pares):
    """
    Calcula, para cada par (origen, destino), la distancia mínima usando
    Dijkstra. Si un origen fue eliminado del grafo, la distancia se
    considera infinita.
    """
    cache = {}
    resultados = {}

    for origen, destino in pares:

        # Si el origen ya no existe (porque fue eliminado)
        if origen not in grafo:
            resultados[(origen, destino)] = float("inf")
            continue

        # Ejecutar Dijkstra una sola vez por cada origen
        if origen not in cache:
            distancias, _ = dijkstra(grafo, origen)
            cache[origen] = distancias

        resultados[(origen, destino)] = cache[origen].get(destino, float("inf"))

    return resultados


def formatear_distancia(d):
    return "INF" if d == float("inf") else str(d)


def construir_filas(pares, dist_antes, dist_despues):
    filas = []

    for origen, destino in pares:
        d_antes = dist_antes[(origen, destino)]
        d_despues = dist_despues[(origen, destino)]

        if d_antes == float("inf"):
            estado = "YA ESTABA DESCONECTADO"
            diferencia = "-"
        elif d_despues == float("inf"):
            estado = "DESCONECTADO"
            diferencia = "-"
        elif d_despues > d_antes:
            estado = "MAS LARGA"
            diferencia = str(round(d_despues - d_antes, 2))
        elif d_despues < d_antes:
            estado = "MAS CORTA"
            diferencia = str(round(d_despues - d_antes, 2))
        else:
            estado = "SIN CAMBIO"
            diferencia = "0"

        filas.append({
            "origen": origen,
            "destino": destino,
            "antes": formatear_distancia(d_antes),
            "despues": formatear_distancia(d_despues),
            "diferencia": diferencia,
            "estado": estado,
        })

    return filas


def imprimir_tabla(filas):
    encabezados = ["Origen", "Destino", "Dist. antes", "Dist. despues", "Diferencia", "Estado"]
    anchos = [8, 8, 12, 14, 11, 24]

    def linea_sep():
        return "+" + "+".join("-" * a for a in anchos) + "+"

    def fila_texto(valores):
        return "|" + "|".join(f" {str(v):<{a - 1}}" for v, a in zip(valores, anchos)) + "|"

    print("\n" + linea_sep())
    print(fila_texto(encabezados))
    print(linea_sep())
    for f in filas:
        print(fila_texto([f["origen"], f["destino"], f["antes"], f["despues"], f["diferencia"], f["estado"]]))
    print(linea_sep())


def main():

    print("===== IMPACTO DEL CIERRE DE UNA ESTACIÓN EN LA RED =====\n")

    # 1) Leer el grafo original
    grafo = ingreso_grafo()

    # 2) Pedir los pares origen-destino a analizar (mínimo 5)
    pares = ingreso_pares(grafo)

    # 3) Calcular las distancias ANTES del cierre (se usa una copia, para no
    #    perder el grafo original antes de aplicar el cierre)
    grafo_antes = deepcopy(grafo)
    dist_antes = calcular_distancias_pares(grafo_antes, pares)

    # 4) Preguntar qué se va a cerrar
    print("\n¿Qué desea cerrar?")
    print("1. Una estación (nodo)")
    print("2. Una conexión (arista)")
    print("3. No cerrar nada")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        nodo = input("Ingrese la estación a cerrar: ").upper()
        if nodo not in grafo:
            print("La estación no existe.")
            return
        eliminar_nodo(grafo, nodo)

    elif opcion == "2":
        origen_c = input("Origen de la conexión: ").upper()
        destino_c = input("Destino de la conexión: ").upper()
        if origen_c not in grafo or destino_c not in grafo:
            print("Algún nodo no existe.")
            return
        eliminar_arista(grafo, origen_c, destino_c)

    elif opcion != "3":
        print("Opción inválida.")
        return

    # 5) Calcular las distancias DESPUÉS del cierre sobre el grafo modificado
    dist_despues = calcular_distancias_pares(grafo, pares)

    # 6) Construir y mostrar la tabla comparativa pedida en el enunciado:
    #    origen, destino, distancia antes, distancia después, diferencia, estado
    filas = construir_filas(pares, dist_antes, dist_despues)

    print("\n===== TABLA COMPARATIVA (ANTES vs. DESPUÉS DEL CIERRE) =====")
    imprimir_tabla(filas)


if __name__ == "__main__":
    main()
