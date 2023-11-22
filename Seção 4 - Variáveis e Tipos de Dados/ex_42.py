# Receba o sálario-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele para 7% de imposto sobre o salário-base.

resp_num = 0

while resp_num == 0:
    try:
        salario_base = float(input("Insira o valor do salário-base: R$ "))
        gratificacao = 0.05
        imposto = 0.07

        total_salario = salario_base + (salario_base * (gratificacao - imposto))
        print(f"\nTOTAL DE FECHAMENTO DE FOLHA: R$ {total_salario:.2f}")
        
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")