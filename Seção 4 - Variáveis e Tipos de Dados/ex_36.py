# Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume de um cilindro circular é calculado por meio da seguinte fórmula: V = π * raio² * altura, onde π = 3,141592.

resp_num = 0

while resp_num == 0:
    try:
        pi = 3.141592
        altura = float(input("Digite a altura do cilindro: "))
        raio = float(input("Digite o valor do raio da base do cilindro: "))

        volume = pi * (raio ** 2) * altura

        print(f"O volume do cilindro de altura {altura} e raio {raio} é {volume:.2f}")
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")