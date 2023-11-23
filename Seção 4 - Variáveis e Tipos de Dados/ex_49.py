# Faça um programa que leia o horário (hora, minuto e segundo) de inicio e a duração, em segundos , de uma experiência biológica. O programa deve resultar no novo horário (hora, minuto e segundo) do término da mesma.

resp_num = 0

while resp_num == 0:
    try:
        h_i = int(input("Digite a hora: "))
        m_i = int(input("Digite os minutos: "))
        s_i = int(input("Digite os segundos:"))
        duracao = int(input("\nDigite a duração da experiência em segundos: "))

            
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")