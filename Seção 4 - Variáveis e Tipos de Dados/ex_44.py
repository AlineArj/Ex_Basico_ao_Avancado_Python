# Receba a altura do degrau de uma escada e a altura que o usuário deseja alcaçar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.

resp_num = 0

while resp_num == 0:
    try:
        h_final = float(input("Digite a altura que se deseja subir: "))
        h_degrau = float(input("Digite a altura do degrau desejado: "))

        total_degraus = int(h_final / h_degrau)
        print(f"\nTotal de degraus necessários: {total_degraus}")

        if (h_final % h_degrau) > 0:
            print(f"\nOBS: Restou {(h_final % h_degrau):.2f} para alcançar a altura de {h_final} o degrau escolhido de {h_degrau}")
            print(f"Para manter a quantidade de {total_degraus} degraus a sua altura deve ser de {(h_final / total_degraus):.2f}")
            print("Caso prefira, altere os parametros escolhidos!")
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")