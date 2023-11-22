# Leia um valor de massa em quilogramas e apresente-o convertido em libras. 
# A fórmula de conversão é: 
# L = K / 0,45 
# Sendo K a massa em quilogramas e L a massa em libras.

resp_num = 0

while resp_num == 0:
    try:
        quilogramas = float(input("Digite o valor da massa (em Kg): "))
        libras = quilogramas / 0.45
        print(f"\n{quilogramas:.2f} Kg é equivalente a {libras:.2f} L")
        
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")