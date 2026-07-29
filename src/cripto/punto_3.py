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
