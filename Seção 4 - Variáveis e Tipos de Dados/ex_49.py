# Faça um programa que leia o horário (hora, minuto e segundo) de inicio e a duração, em segundos , de uma experiência biológica. O programa deve resultar no novo horário (hora, minuto e segundo) do término da mesma.

resp_num = 0

while resp_num == 0:
    try:
        h_i = int(input("Digite a hora: "))
        m_i = int(input("Digite os minutos: "))
        s_i = int(input("Digite os segundos: "))
        d = int(input("\nDigite a duração da experiência em segundos: "))

        if d > 3599:
            h_f = h_i + int(d / 3600)
            d %= 3600
        else:
            h_f = h_i

        if d > 59:
            m_f = m_i + int(d / 60)
            d %= 60
        else:
            m_f = m_i
        
        s_f = s_i + d

        print(f"A experiência irá acabar as {h_f:.0f}:{m_f:.0f}:{s_f:.0f}")
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")