# Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³. 
# A fórmula de conversão é: 
# m = L / 1000 
# Sendo L o valume em litros e m o volume em metros cúbicos.

resp_num = 0

while resp_num == 0:
    try:
        litros = float(input("Digite um volume em litros: "))
        metros = litros / 1000
        print(f"\n{litros:.2f}L é equivalente a {metros:.2f} m³")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")