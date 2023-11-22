# Leia um número real e imprima o resultado do quadrado desse número.

resp_num = 0

while resp_num == 0:
    try:
        num_inp = float(input("Digite um número real: "))
        quadrado = num_inp ** 2
        print(f"\nO quadrado de {num_inp} é {quadrado:.2f}")
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")