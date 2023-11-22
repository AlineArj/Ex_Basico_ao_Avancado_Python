# Leia um valor de área em metros quadrados m² e apresente-o convertido em acres. 
# A fórmula de conversão é: 
# A = m * 0,0002471
# Sendo m a área em metros quadrados e A a área em acres.

resp_num = 0

while resp_num == 0:
    try:
        metros = float(input("Digite o valor da área em m²: "))
        acres = metros * 0.000247
        print(f"{metros:.2f} m² é equivalente a {acres:.2f} ac")
        
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")