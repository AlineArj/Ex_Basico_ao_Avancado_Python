# Leia um ângulo em graus e apresente-o convertido em radianos. 
# A fórmula de conversão é: 
# R = G * π / 180
# Sendo π = 3,1415
#*******
resp_num = 0
pi = 3.1415

while resp_num == 0:
    try:
        graus = float(input("Digite um ângulo em graus: "))
        radianos = graus *  (pi / 180)
        print(graus / 180)
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")