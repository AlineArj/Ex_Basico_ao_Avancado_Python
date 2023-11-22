# Leia um valor de massa em libras e apresente-o convertido em quilogramas. 
# A fórmula de conversão é: 
# K = L * 0,45  
# Sendo K a massa em quilogramas e L a massa em libras.

resp_num = 0

while resp_num == 0:
    try:
        libras = float(input("Digite o valor da massa (em libras): "))
        quilogramas = libras * 0.45
        print(f"\n{libras:.2f} L é equivalente a {quilogramas:.2f} Kg")
        
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")