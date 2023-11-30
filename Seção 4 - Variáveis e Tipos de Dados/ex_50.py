# Impremente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.

from datetime import date


resp_num = 0

while resp_num == 0:
    try:
        ano_atual = date.today().year
        idade = int(input("Digite a sua idade atual: "))

        print(f"\nVocê nasceu em {ano_atual - idade}!")
        resp_num = 1

    except:
        print("\nInválido!\n")