#joguinho de dados
from random import randint
from time import sleep
from operator import itemgetter
rodadas=int(input("Quantas rodadas você quer fazer?")) # recebi quantas rodadas quiser jogar
vitorias = [0, 0, 0, 0]
for i in range(rodadas): 
   jogo=dict()
   rodada = [randint(1,6), randint(1,6), randint(1,6), randint(1,6),] # faz números aleatorios pra os jogadores
   for i in range(1,5):
      jogo[i] = rodada[i-1]
   ranking= list() # faz uma lista com o ranking dos jogadores
   print("Roll the dice!")
   for u, m in jogo.items():
      print(f"O {u}º jogador tirou {m} no dado.") 
      sleep(1)
   ranking= sorted(jogo.items(), key=itemgetter(1), reverse=True)
   print("-=" * 20)
   print("   ** RANKING DOS JOGADORES **")
   for h, t in enumerate(ranking):
      if  t[1] == max(rodada):
         vitorias[t[0]-1] += 1
      print(f"    {h+1}º lugar: Jogador {t[0]} com {t[1]} no dado.")
      sleep(1)
vencedores = list() # faz uma lista com os vencedores 
for i, valor in enumerate(vitorias):
   if valor == max(vitorias):
      vencedores.append(i+1)
if len(vencedores) == 1: # calcula os vencedores e se tiver empate, mostra quem venceu e se deu empate
   print(f'Vencedor: Jogador Nº{vencedores[0]}. ')
elif len(vencedores) == 2:
   print(f'Vencedores: Jogador Nº {vencedores[0]} e Jogador Nº {vencedores[1]}. ')
elif len(vencedores) == 3:
   print(f'Vencedores: Jogador Nº {vencedores[0]}, Jogador Nº {vencedores[1]} e Jogador Nº {vencedores[2]}. ')  
else:
   print('Os 4 Jogadores empataram.')