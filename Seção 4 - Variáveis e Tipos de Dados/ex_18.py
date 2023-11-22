# Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros. 
# A fórmula de conversão é: 
# L = 1000 * m
# Sendo L o vaolume em litros e m o volume em metros cúbicos.

resp_num = 0

while resp_num == 0:
    try:
        metros = float(input("Digite um volume em m³: "))
        litros = 1000 * metros
        print(f"\n{metros:.2f} m³ é equivalente a {litros:.2f}L")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")