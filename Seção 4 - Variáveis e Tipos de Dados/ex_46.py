# Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere outro número formado pelos dígitos invertidos do número lido. Exemplo: Número lido -> 123 Número gerado -> 321

resp_num = 0

while resp_num == 0:
    try:
        num_inp = int(input("Insira um número entre 100 e 999: "))

        if 100 <= num_inp <= 999:
            centena = int(num_inp / 100)
            dezena = int((num_inp % 100) / 10)
            unidade = (num_inp % 100) % 10
            
            novo_num = str(unidade) + str(dezena) + str(centena)
            print(f"\nNúmero gerado: {novo_num}")

        else:
            num_inp = int('x')
        
        resp_num = 1

    except:
        print("\n /!\ Erro: Valor inválido /!\ \n")