# Leia uma temperatura em graus Celcius e apresente-a convertida em graus Kelvin. 
# A fórmula de conversão é: 
# K = C + 273,15

resp_num = 0

while resp_num == 0:
    try:
        temp_c = float(input("Digite uma temperatura em graus Celsius: "))
        temp_k = temp_c + 273.15
        print(f"A temperatura {temp_c:.2f} ºC é equivalente a {temp_k:.2f} K")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")