# Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância da origem (0, 0).

resp_num = 0

while resp_num == 0:
    try:
        x = float(input("Digite uma coordenada em x: "))
        y = float(input("Digite uma coordenada em y: "))

        d = (( x ** 2) + (y ** 2)) ** (1/2)

        print(f"\nA distência da origem é de {d:.2f}")
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")