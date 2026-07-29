import random
MODULO = 1000003
def dividir_secreto(numero):
    parte1 = random.randint(0, MODULO - 1)
    parte2 = random.randint(0, MODULO - 1)

    parte3 = (numero - parte1 - parte2) % MODULO

    return parte1, parte2, parte3
p1, p2, p3 = dividir_secreto(40)

print(p1)
print(p2)
print(p3)

print((p1+p2+p3)%MODULO)
