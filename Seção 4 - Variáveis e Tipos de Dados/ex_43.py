# Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre: 
# * O total a pagar a vista com desconto de 10%; 
# * O valor de cada parcela, no parcelamento de 3x sem juros; 
# * A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto); 
# * A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total).

resp_num = 0

while resp_num == 0:
    try:
        desconto = 0.1
        comissão = 0.05
        total_inp = float(input("Digite o valor da compra: R$ "))

        print(f"""\n{'#' * 12} A VISTA {'#' * 12}\nTotal a receber: R$ {(total_inp * (1 - desconto)):.2f}\nComissão do vendedor: R$ {(total_inp * (1 - desconto) * comissão):.2f}\n{'-' * 40}\n{'#' * 12} PARCELADO {'#' * 12}\nTotal da parcela (3x sem juros): R$ {(total_inp / 3):.2f}\nComissão do vendedor: R$ {(total_inp * comissão):.2f}\n""")
        
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")