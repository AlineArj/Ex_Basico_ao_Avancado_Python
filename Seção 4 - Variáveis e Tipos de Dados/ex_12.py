# Leia uma distância em milhas e apresente-a convertida em quilômetros. 
# A fórmula de conversão é: 
# K = 1,61 * M

resp_num = 0

while resp_num == 0:
    try:
        milha = float(input("Digite uma velocidade em Milhas: "))
        quilometro = milha * 1.61
        print(f"{milha:.1f} M = {quilometro:.1f} Km")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")