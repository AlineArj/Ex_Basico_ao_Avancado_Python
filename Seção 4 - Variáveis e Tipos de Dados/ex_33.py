# Leia o tamanho do lado de quadrado e imprima como resultado a sua área.

resp_num = 0

while resp_num == 0:
    try:
        lado = float(input("Digite o tamanho do lado do quadrado: "))
        print(f"\nA área do quadrado de lado {lado:.1f} é {(lado * lado):.1f}")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")