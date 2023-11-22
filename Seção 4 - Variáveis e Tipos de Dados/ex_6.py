# Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. 
# A fórmula de conversão é: 
# F = C * (9 / 5) + 32

resp_num = 0

while resp_num == 0:
    try:
        temp_c = float(input("Digite uma temperatura em graus Celsius: "))
        temp_f = temp_c * (9 / 5) + 32
        print(f"\nA temperatura {temp_c:.2f} ºC é equivalente a {temp_f:.2f} ºF")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")