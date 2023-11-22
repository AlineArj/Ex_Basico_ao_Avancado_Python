# Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares. 
# A fórmula de conversão é: 
# H = m * 0,0001 
# Sendo m a área em metros quadrados e H a área em hectares.

resp_num = 0

while resp_num == 0:
    try:
        metros = float(input("Digite uma área em m²: "))
        hectares = metros * 0.0001
        print(f"{metros:.2f} m² é equivalente a {hectares:.2f} ha")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")