# Leia uma velocidade em m/s e apresente-a convertida em Km/h. 
# A fórmula de conversão é: 
# Km/h = m/s * 3,6

resp_num = 0

while resp_num == 0:
    try:
        metro = float(input("Digite uma velocidade em m/s: "))
        quilometro = metro * 3.6
        print(f"{metro:.1f} m/s = {quilometro:.1f} Km/h")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")