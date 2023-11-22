# Leia um valor de comprimento em centímetros e apresente-o convertido em  polegadas. 
# A fórmula de conversão é: 
# P = c / 2,54
# Sendo c o comprimento em centímetro e P o comprimento em polegadas.

resp_num = 0

while resp_num == 0:
    try:
        centimetros = float(input("Digite um comprimento em centimetros: "))
        polegadas = centimetros / 2.54
        print(f"""\n{centimetros:.2f} cm é equivalente a {polegadas:.2f}" """)

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")