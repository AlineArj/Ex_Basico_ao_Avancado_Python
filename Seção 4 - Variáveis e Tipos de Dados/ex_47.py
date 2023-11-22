# Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima um dígito por linha.

resp_num = 0

while resp_num == 0:
    try:
        num_inp = int(input("\nDigite um número entre 1000 a 9999: "))

        if 1000 <= num_inp <= 9999:
            milhar = int(num_inp / 1000)
            centena = int((num_inp % 1000) / 100)
            dezena = int(((num_inp % 1000) % 100) / 10)
            unidade = int(((num_inp % 1000) % 100) % 10)

            print(f"{milhar}\n{centena}\n{dezena}\n{unidade}")
        else:
            num_inp = int('x')

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.")