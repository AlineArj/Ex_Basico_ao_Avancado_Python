# A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso. Sendo que da quantia total: 
# * O primeiro ganhador receberá 46%; 
# * O segundo receberá 32%; 
# * O terceiro receberá o restante. 
# Calcule e imprima a quantia ganha por cada um dos ganhadores.

resp_num = 0
while resp_num == 0:
    try:
        premio = 780000
        ganhador_1 = 0.46
        ganhador_2 = 0.32
        ganhador_3 = 1 - (ganhador_1 + ganhador_2)

        print(f"""
              Valor total do prêmio: R$ {premio:.2f}
              {"-" * 40}
              O primeiro ganhador receberá R$ {(ganhador_1 * premio):.2f}
              O segundo ganhador receberá R$ {(ganhador_2 * premio):.2f}
              O terceiro ganhador receberá R$ {(ganhador_3 * premio):.2f}""") 

        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")