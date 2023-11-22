# Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, 
# sabendo que ele recebeu um aumento de 25%.

resp_num = 0

while resp_num == 0:
    try:
        aumento = 0.25
        salario = float(input("Digite o valor atual do salário: "))
        print(f"\nO novo salário com {(aumento * 100)}% de aumento: R$ {(salario * (1 + aumento)):.2f}")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")