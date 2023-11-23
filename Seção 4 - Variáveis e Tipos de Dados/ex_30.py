# Leia um valor em real e cotação do dólar. Em seguida, imprima o valor correspondente em dólares.

resp_num = 0

while resp_num == 0:
    try:
        real = float(input("Digite o valor a ser convertido: R$ "))
        cot_dolar = float(input("Digite a cotação atual do dolar: R$ "))

        dolar = real / cot_dolar
        
        print(f"\nR$ {real:.2f} = $ {dolar:.2f}")
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")