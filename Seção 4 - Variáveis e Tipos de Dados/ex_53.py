# Faça um programa para ler as dimensões de um terreno (comprimento c e largura l), bem como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno com tela.

resp_num = 0

while resp_num == 0:
    try:
        c = float(input("Digite o comprimento em metro do terreno: "))
        l = float(input("Digite a largura em metro do terreno: "))
        preco = float(input("Digite o preço do metro da tela: "))

        print(f"\nO valor da tela para um terreno de {l:.0f}x{c:.0f} é de R$ {((c * l) * preco):.2f}")
        resp_num = 1

    except:
        print("\nInválido! Tente novamente.\n")