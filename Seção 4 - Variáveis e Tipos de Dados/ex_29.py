# Leia quatro notas, calcule a média aritmética e imprima o resultado.

resp_num = 0

while resp_num == 0:
    try:
        nota_1 = float(input("Digite o valor da primeira nota: "))
        nota_2 = float(input("Digite o valor da segunda nota: "))
        nota_3 = float(input("Digite o valor da terceira nota: "))
        nota_4 = float(input("Digite o valor da quarta nota: "))

        media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
        print(f"\nA média artmética é: {media:.1f}")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")