# Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.

resp_num = 0

while resp_num == 0:
    try:
        num_1 = float(input("Digite o primeiro número: "))
        num_2 = float(input("Digite o segundo número: "))
        num_3 = float(input("Digite o terceiro número: "))

        soma = (num_1 ** 2) + (num_2 ** 2) + (num_3 ** 2)
        print(f"\n{num_1:.1f}² + {num_2:.1f}² + {num_3:.1f}² = {soma:.1f}")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")