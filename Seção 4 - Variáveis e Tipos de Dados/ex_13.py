# Leia uma distância em quilômetros e apresente-a convertida em milhas. 
# A fórmula da conversão é: 
# M = K / 1,61

resp_num = 0

while resp_num == 0:
    try:
        quilometro = float(input("Digite uma velocidade em Km/h: "))
        milha = quilometro / 1.61
        print(f"{quilometro:.1f} Km = {milha:.1f} M")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")