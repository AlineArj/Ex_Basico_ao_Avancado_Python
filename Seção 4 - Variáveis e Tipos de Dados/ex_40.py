# Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima a quatia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.

pag_dia = 30
imposto_renda = 0.08

resp_num = 0

while resp_num == 0:
    try:
        dias_trabalhados = int(input("Insira quantos dias serão trabalhados: "))
        total_pago = ((1 - imposto_renda) * pag_dia * dias_trabalhados)
        
        print(f"\nPara {dias_trabalhados} dias trablhados deverá ser pago o valor de R${total_pago:.2f}.")

        resp_num = 1
    except:
        print(f"\nInválido, tente novamente.\n")