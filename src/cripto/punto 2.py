def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def inverso_modular(e, phi):
    # Algoritmo extendido de Euclides
    r0, r1 = phi, e
    s0, s1 = 0, 1

    while r1 != 0:
        cociente = r0 // r1
        r0, r1 = r1, r0 - cociente * r1
        s0, s1 = s1, s0 - cociente * s1

    # s0 es el inverso de e módulo phi (puede ser negativo)
    return s0 % phi


def cifrar(mensaje, e, n):
    return pow(mensaje, e, n)


def descifrar(cifrado, d, n):
    return pow(cifrado, d, n)


def main():
    print("RSA DE JUGUETE ")

    p = int(input("Ingrese p: "))
    q = int(input("Ingrese q: "))
    e = int(input("Ingrese e: "))
    mensaje = int(input("Ingrese el mensaje: "))
# lo que se pide cálcular en el taller
    n = p * q
    phi = (p - 1) * (q - 1)

    if mcd(e, phi) != 1:
        print("\nError: e no es válido porque no es coprimo con phi(n).")
        return

    d = inverso_modular(e, phi)

    cifrado = cifrar(mensaje, e, n)
    descifrado = descifrar(cifrado, d, n)
# resultados que se van a generar (osea todo lo que se pidio en el taller)
    print("\nRESULTADOS ")
    print(f"n = {n}")
    print(f"phi(n) = {phi}")
    print(f"d = {d}")
    print(f"Cifrado = {cifrado}")
    print(f"Descifrado = {descifrado}")


if __name__ == "__main__":
    main()