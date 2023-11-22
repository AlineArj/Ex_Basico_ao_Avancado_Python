# Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
# A fórmula de conversão é: 
# C = 5 * (F - 32) / 9

resp_num = 0

while resp_num == 0:
    try:
        temp_f = float(input("Digite uma temperatura em graus Fahrenheit: "))
        temp_c = 5 * (temp_f - 32) / 9
        print(f"A temperatura {temp_f:.2f} ºF é equivalente a {temp_c:.2f} ºC")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")