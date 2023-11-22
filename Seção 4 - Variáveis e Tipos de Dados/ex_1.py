# Faça um programa que leia um número inteiro e imprima.

resp_num = 0

while resp_num == 0:
    try:
        num_inp = int(input("Digite um número inteiro: "))
        print("\nO número escolhido foi: ", num_inp)
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")