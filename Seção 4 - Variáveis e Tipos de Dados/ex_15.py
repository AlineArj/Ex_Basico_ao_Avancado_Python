# Leia um ângulo em radianos e apresente-o convertido em graus. 
# A fórmula de conversão é: 
# G = R * 180 / π 
# Sendo π = 3,1415
#*******
resp_num = 0
pi = 3.1415

while resp_num == 0:
    try:
        radianos = float(input("Digite um ângulo em radianos: "))
        graus = radianos * (180 / pi)
        print(graus)
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")