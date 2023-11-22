# Leia um valor inteiro em segundo e imprima-o em horas, minutos e segundos

resp_num = 0

while resp_num == 0:
    try:
        num_inp = int(input("Digite o tempo em segundos: "))
        
        horas = int(num_inp / 3600)
        minutos = int((num_inp % 3600) / 60)
        segundos = int((num_inp % 3600) % 60)
        print(f"\n{horas}h {minutos}m {segundos}s")

        resp_num = 1

    except:
        print("\n /!\ Erro: Valor inválido /!\ \n")