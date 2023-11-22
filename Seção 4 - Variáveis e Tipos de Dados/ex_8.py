# Leia uma temperatura em Kelvin eapresente-a convertida em graus Celsius. 
# A fórmula de conversão é: 
# C = K - 273,15

resp_num = 0

while resp_num == 0:
    try:
        temp_k = float(input("Digite uma temperatura em Kelvin: "))
        temp_c = temp_k - 273.15
        print(f"A temperatura {temp_k:.2f} K é equivalente a {temp_c:.2f} ºC")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")