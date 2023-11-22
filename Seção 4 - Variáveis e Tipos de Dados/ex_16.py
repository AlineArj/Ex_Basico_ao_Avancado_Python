# Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros. 
# A fórmula de conversão: 
# c = P * 2,54
# Sendo c o comprimento em centímetros e P o comprimento em polegadas. 

resp_num = 0

while resp_num == 0:
    try:
        polegadas = float(input("Digite um comprimento em polegadas: "))
        centimetros = polegadas * 2.54
        print(f"""\n{polegadas:.2f}"  é equivalente a {centimetros:.2f} cm""")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")