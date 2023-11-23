# Leia o valor do raio de um círculo e calcule e imprima a área do círculo correpondente. 
# A área do cículo é π * raio², considere π = 3,141592.

resp_num = 0

while resp_num == 0:
    try:
        pi = 3.141592
        raio = float(input("Digite o valor do raio do círculo: "))

        area = pi * (raio ** 2)

        print(f"A área do círculo de raio {raio} é {area:.2f}")
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")