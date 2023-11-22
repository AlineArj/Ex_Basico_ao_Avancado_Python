# Leia uma velocidade em Km/h e apresente-a convertida em m/s. 
# A fórmula de conversão é: 
# m/s = Km/h / 3,6

resp_num = 0

while resp_num == 0:
    try:
        quilometro = float(input("Digite uma velocidade em Km/h: "))
        metro = quilometro / 3.6
        print(f"{quilometro:.1f} Km/h = {metro:.1f} m/s")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")