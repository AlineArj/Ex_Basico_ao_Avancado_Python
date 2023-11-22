# Leia um valor de área em acres e apresente-o convertido em metros quadrados m². 
# A fórmula de conversão é:
# m = A * 4046,86
# Sendo m a área em metros quadrados e A a área em acres.

resp_num = 0

while resp_num == 0:
    try:
        acres = float(input("Digite o valor da área em acres: "))
        metros = acres * 4046.86
        print(f"{acres:.2f} ac é equivalente a {metros:.2f} m²")
        
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")