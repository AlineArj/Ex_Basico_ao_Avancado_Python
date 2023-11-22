# Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.

resp_num = 0

while resp_num == 0:
    try:
        num = int(input("Digite um número inteiro: "))
        resultado = ((num * 3) + 1) + ((num * 2) - 1)
        print(f"\n(({num} * 3) + 1) + (({num} * 2) - 1) = {resultado}")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")