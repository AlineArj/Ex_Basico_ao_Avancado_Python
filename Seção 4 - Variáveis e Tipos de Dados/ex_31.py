# Leia um número inteiro e imprima o seu antecessor e o seu sucessor.

resp_num = 0

while resp_num == 0:
    try:
        num = int(input("Digite um número inteiro: "))
        print(f"\n{num - 1} e {num + 1}")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")