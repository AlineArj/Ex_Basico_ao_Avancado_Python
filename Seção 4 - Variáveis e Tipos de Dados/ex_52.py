# Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que dada um deu para a realização da aposta. Faça um programa que leia quanto cada aopstador investiu, o valor do prêmio e imprima quanto cada um ganharia do prêmio com base no valor investido.

resp_num = 0

while resp_num == 0:
    try:
        jogador_1 = float(input("Valor apostado pelo primeiro jogador: R$ "))
        jogador_2 = float(input("Valor apostado pelo segundo jogador: R$ "))
        jogador_3 = float(input("Valor apostado pelo terceiro jogador: R$ "))
        premio = float(input("\nValor do prêmio: R$ "))

        aposta = jogador_1 + jogador_2 + jogador_3

        print(f"\n{' ' * 6}PRÊMIAÇÃO{' ' * 6}")
        print(f"1º Jogador: R$ {(premio * (jogador_1 / aposta)):.2f}\n2º Jogador: R$ {(premio * (jogador_2 / aposta)):.2f}\n3º Jogador: R$ {(premio * (jogador_3 / aposta)):.2f}")

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")