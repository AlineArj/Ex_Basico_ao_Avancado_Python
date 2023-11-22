# Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.

resp_num = 0 

while resp_num == 0:
    try:
        valor_trab = float(input("Digite o valor da hora de trabalho em reais: "))
        hora_trab = float(input("Digite o tempo trabalhando em horas: "))
        adicional = 0.1
        
        salario = (1 + adicional) * valor_trab * hora_trab
        print(f"\nTotal a pagar: R$ {salario:.2f}.")

        resp_num = 1

    except:
        print("\n /!\ Erro: Valor inválido /!\ \n")