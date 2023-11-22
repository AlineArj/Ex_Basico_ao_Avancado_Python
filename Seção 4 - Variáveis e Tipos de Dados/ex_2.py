# Faça um programa que leia um número real e o imprima.

resp_num = 0

while resp_num == 0:
    try:
        num_inp = float(input("Digite um número real: "))
        print("\nO número escolhido foi: ", num_inp)
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")