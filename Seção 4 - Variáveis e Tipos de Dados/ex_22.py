# Leia um valor de comprimento em jardas e apresente-o convertido em metros. 
# A fórmula de conversão é: 
# m = 0,91 * J 
# Sendo J o comprimento em jardas e m o comprimento em metros.

resp_num = 0

while resp_num == 0:
    try:
        jardas = float(input("Digite um comprimento em jardas: "))
        metros = 0.91 * jardas
        print(f"\n{jardas:.2f} J é equivalente a {metros:.2f} m")
        
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")