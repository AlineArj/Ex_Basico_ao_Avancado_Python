# Peça a um usuário para digitar três valores inteiros e imprima a soma deles.

resp_num = 0

while resp_num == 0:
    try:
        print("Digite três números inteiros.")

        num_inp_1 = int(input("Número 1: "))
        num_inp_2 = int(input("Número 2: "))
        num_inp_3 = int(input("Número 3: "))

        soma = num_inp_1 + num_inp_2 + num_inp_3

        print("\n", num_inp_1, "+", num_inp_2, "+", num_inp_3, "=", soma)
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")