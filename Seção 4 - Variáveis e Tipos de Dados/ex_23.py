# Leia um valor de comprimento em metros e apresente-o convertido em jardas. 
# A fórmula de conversão é: J = m / 0,91 
# Sendo J o comprimento em jardas e m o comprimento em metros.

resp_num = 0

while resp_num == 0:
    try:
        metros = float(input("Digite um comprimento em metros: "))
        jardas = metros / 0.91
        print(f"\n{metros:.2f} m é equivalente a {jardas:.2f} J")
        
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")