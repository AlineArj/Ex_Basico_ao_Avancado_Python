# Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%.

resp_num = 0

while resp_num == 0:
    try:
        desconto = 0.12
        valor = float(input("Digite o valor do produto: "))
        print(f"\nO valor com {desconto * 100}% de desconto fica em R$ {(valor * (1 - desconto)):.2f}")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")