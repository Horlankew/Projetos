from random import randint
from time import sleep

print("          \n*-*                *-*\n       JO-KEN-PÔ   ")
resposta = "S"
voce_venceu = bot_venceu = empate = 0
while True:
    rodadas=int(input("Quantas rodadas você quer jogar? "))
    for c in range(rodadas):
        pedra = ("Pedra")
        papel = ("Papel")
        tesoura = ("Tesoura")
        opcoes = (pedra, papel, tesoura)
        computador = randint(0, 2)
        print(('''------JOKENPÔ------
    Escolha sua jogada:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''' ))
        jogador = ""
        jokenpo = [0, 1, 2]
        jogador = int(input(" Sua Vez! : "))
        while jogador not in jokenpo:
            jogador = int(input('''Digite uma opção de acordo com: \n    
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA. \nQual é a sua jogada? '''))
        print("Computador jogando!")
        sleep(1)
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PÔÔÔ!")
        sleep(1)
        print(f"  Computador jogou [ {opcoes[computador]} ].")
        print(f"  Você jogou [ {opcoes[jogador]} ].")
        if computador == 0:#contabiliza as jogadas
            if jogador == 0:
                print("\nEmpate!! -_-")
                empate += 1
            elif jogador == 1:
                print("\nVocê venceu. \o/")
                voce_venceu += 1
            elif jogador == 2:
                bot_venceu += 1
                print("\nComputador venceu. =(")
        elif computador == 1:
            if jogador == 0:
                print("\nComputador venceu. =(")
                bot_venceu += 1
            elif jogador == 1:
                print("\nEmpate!! -_-")
                empate += 1
            elif jogador == 2:
                print("\nVocê venceu. \o/")
                voce_venceu += 1
        elif computador == 2:
            if jogador == 0:
                print("\nVocê venceu. \o/")
                voce_venceu += 1
            elif jogador == 1:
                print("\nComputador venceu. =(")
                bot_venceu += 1
            elif jogador == 2:
                print("\nEmpate!! -_-")
                empate += 1
        print(f'''x=x=x=x    PONTUAÇÃO ATUAL   =x=x=x=x=
        Você    \o/ [ {voce_venceu} ] \o/
        Computador  [ {bot_venceu} ]''')   # mostra a pontuação de cada rodada
         #resultado do joguinho
        if voce_venceu > bot_venceu:
                print(f"\nVocê venceu \o/ \nPor [{voce_venceu}] a [{bot_venceu}].")
        elif voce_venceu < bot_venceu:
            print(f'\nO computador venceu você =(\nPor [{bot_venceu}] a [{voce_venceu}] , não fique triste jogue novamente pra vencer.')
        elif voce_venceu == bot_venceu:
            print(f'\nEmpate.')
    resposta = str(input("\nDeseja continuar a jogar ? [S/N] ")).upper().strip()[0]
    while resposta not in 'SN':#pergunta se quer continuar o joguinho
        resposta = str(input("Digite uma opção válida. Deseja continuar a jogar ? [S/N] ")).upper().strip()[0]
    if resposta == "N":
        break