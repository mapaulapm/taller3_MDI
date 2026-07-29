import random
MODULO = 1000003
#construcción de servidores individuales
def dividir_secreto(numero):
    parte1 = random.randint(0, MODULO - 1)
    parte2 = random.randint(0, MODULO - 1)

    parte3 = (numero - parte1 - parte2) % MODULO

    return parte1, parte2, parte3
p1, p2, p3 = dividir_secreto(40)
# construir 3 servidores 
def crear_servidores(notas):
    servidor1 = []
    servidor2 = []
    servidor3 = []

    for nota in notas:
        p1, p2, p3 = dividir_secreto(nota)

        servidor1.append(p1)
        servidor2.append(p2)
        servidor3.append(p3)

    return servidor1, servidor2, servidor3
# suma de las notas
def reconstruir_suma(s1, s2, s3):
    suma = 0

    for i in range(len(s1)):
        suma += (s1[i] + s2[i] + s3[i]) % MODULO

    return suma

# nota promedio
def calcular_promedio(suma, cantidad):
    return suma / cantidad
def main():
    entrada = input("Ingrese las notas separadas por espacios: ")
    notas = list(map(int, entrada.split()))

    s1, s2, s3 = crear_servidores(notas)

    print("Servidor 1:", s1)
    print("Servidor 2:", s2)
    print("Servidor 3:", s3)

    suma = reconstruir_suma(s1, s2, s3)
    promedio = calcular_promedio(suma, len(notas))

    print("\nResultados")
    print("Suma:", suma)
    print("Promedio:", promedio)

if __name__ == "__main__":
    main()