# Leia um valor de área em hectares e apresente-o convertido em metros quadrados m². 
# A fórmula de conversão é: m = H * 10000 
# Sendo m a área em metros quadrados e H a área em hectares.

resp_num = 0

while resp_num == 0:
    try:
        hectares = float(input("Digite uma área em hectares: "))
        metros = hectares * 10000
        print(f"{hectares:.2f} ha é equivalente a {metros:.2f} m²")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")