# Leia um número real e imprima a quinta parte deste número.

resp_num = 0

while resp_num == 0:
    try:
        num_inp = float(input("Digite um número real: "))
        num_parte = num_inp / 5
        print(f"\nA quinta parte de {num_inp} é {num_parte:.2f}")
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")