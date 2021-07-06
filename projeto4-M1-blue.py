from os import system #limpa o codigo
from time import sleep
from datetime import date
#\033[??m da cores na hora de imprimir \033[m finaliza a cor que determinei, \U0001F499 alguns emojis
# função que verifica as condição dos eleitores através da idade do eleitor, se é opcional,obrigatório ou negado seu voto.
def autoriza_voto(ano):
    atual= date.today().year
    idade= atual - ano
    if idade < 16:
        return f'NEGADO'
    elif 16 <= idade < 18 or idade > 70:
        return f'OPCIONAL.'
    else:
        return f'OBRIGATÓRIO.'


# função que autoriza ou não os eleitores a votarem, se o voto for obrigatório ou opcional:
# a função faz a contagem dos votos para cada candidato, votos nulos e os em brancos, caso não possa votar ela nega o voto.
def votacao(voto, autorizacao): 
    if  autorizacao == 'NEGADO':
        print("\033[31;107mVocê não pode votar ainda.\033[m \U0001F6AB	")
        sleep(3)
    elif ( autorizacao == 'OPCIONAL.' or  autorizacao == 'OBRIGATÓRIO.') and voto == 1: 
        num[cand[0]]+=1
        print("\033[33mVoto computado.\033[m")
        sleep(2)                                                     
    elif ( autorizacao == 'OPCIONAL.' or  autorizacao == 'OBRIGATÓRIO.') and voto == 2: 
        num[cand[1]]+=1
        print("\033[33mVoto computado.\033[m")
        sleep(2)
    elif ( autorizacao == 'OPCIONAL.' or  autorizacao == 'OBRIGATÓRIO.') and voto == 3:
        num[cand[2]]+=1
        print("\033[33mVoto computado.\033[m")
        sleep(2)
    elif ( autorizacao == 'OPCIONAL.' or  autorizacao == 'OBRIGATÓRIO.') and voto == 4:
        num[cand[3]]+=1
        print("\033[33mVoto computado.\033[m")
        sleep(2)
    elif ( autorizacao == 'OPCIONAL.' or  autorizacao == 'OBRIGATÓRIO.') and voto == 5:
        num[cand[4]]+=1
        print("\033[33mVoto computado.\033[m")
        sleep(2)
    else: 
        num[cand[4]]+= 1
        print("\033[33mVoto computado.\033[m")
        sleep(2)

#print que da início ao programa e da boas vindas as candidatas.
print("\033[32m-=\033[m"*91)
print("\033[32m=-\033[m"*91)
print(f'''\033[35mCandidatas \033[mna eleição de \033[32m2021 \033[m, \033[3;97mvieram especialmente da Terra do amanhecer em Mobile Legends, para as eleições da \033[m\033[41;44m\U0001F499 BLUE ED .\033[m
\033[31;107mPS: se houver apenas um voto por candidata, a candidata que recebeu o 1º voto vence.\033[m
''')
sleep(3)
print('\033[32m.\033[m'*150)
sleep(1)
#prints que mostras as candidatas, suas frases de efeito e descrição.
print(f'''\033[36m
    ┏{"━"*20}┳{"━"*63}┓
    ┃\033[1;31;107m{"NOME":^20}\033[m\033[36m┃\033[1;31;107m{"  DESCRIÇÃO":^63}\033[m\033[36m┃
    \033[36m┣{"━"*20}╋{"━"*63}┫
    ┃\033[7;34;107m{'      " AURORA "':<20}\033[m\033[36m┃\033[7;34;107m{'" A Rainha e maga de Gelo mais poderosa da terra do amanhecer."':^21}\033[m\033[36m┃
    \033[36m┗{"━"*20}┻{"━"*63}┛\033[m
    \033[32mFrase:\033[m\033[1;36;44m AURORA, "Pequeno e Branco, Limpo e Brilhante, CONGELAR!\U0001F499 "\033[m
    ''')
sleep(4)
print('\033[32m.\033[m'*150)
sleep(1)
print(f'''\033[34m
    ┏{"━"*20}┳{"━"*62}┓
    ┃\033[1;31;107m{"NOME":^20}\033[m\033[34m┃\033[1;31;107m{" DESCRIÇÃO":^62}\033[m\033[34m┃
    \033[34m┣{"━"*20}╋{"━"*62}┫
    ┃\033[7;34;107m{'      " NANA "':<20}\033[m\033[34m┃\033[7;34;107m{'    "A gatinha mais fofa da terra do amanhecer."':^62}\033[m\033[34m┃
    \033[34m┗{"━"*20}┻{"━"*62}┛\033[m
    \033[32mFrase:\033[m \033[7;34;107m NANA, "Miau,Miau,Miauuu, Eu também posso fazer magia! \U0001F49C "\033[m
''') 
sleep(4)
print('\033[32m.\033[m'*150)
sleep(1)
print(f'''
    \033[33m
    ┏{"━"*20}┳{"━"*74}┓
    ┃\033[1;31;107m{"NOME":^20}\033[m\033[33m┃\033[1;31;107m{" DESCRIÇÃO":^74}\033[m\033[33m┃
    \033[33m┣{"━"*20}╋{"━"*74}┫
    ┃\033[7;34;107m{'     " WANWAN "':<20}\033[m\033[33m┃\033[7;34;107m{'"A garota é inteligente, ágil e fofa, também sempre tem armas escondidas."':^62}\033[m\033[33m┃
    \033[33m┗{"━"*20}┻{"━"*74}┛\033[m
    \033[32mFrase:\033[m \033[1;33;44m WAN-WAN, "A confiança cega não levará a lugar algum! \U0001F49B "\033[m
''')
sleep(4)

print(f'''\033[32m{"*"*64}\033[m  \033[35;107m\nVote consciente na sua heroína favorita, Bjs da BLUE ED \U0001F499 Amrs.\033[m\n\033[32m{"*"*64}\033[m
''')
sleep(4)
#dicionário com as candidatas,nulo e brancos
cand = ['AURORA', 'NANA', 'WANWAN', 'Nulos', 'Brancos']
num = {cand[0] : 0, cand[1] : 0, cand[2] : 0, cand[3] : 0, cand[4] : 0}
#while True que recebi dos usuários os votos, e encerra o programa quando digitado fim
while True:
    system('cls')
    print('''        \033[32;107m SISTEMA DE VOTAÇÃO \033[m''')
    print('\033[32m.\033[m'*30)
    sleep(1)
# indica os números pra os eleitores votarem nas candidatas, nulos ou brancos 
    print('''\033[32m\nCANDIDATAS\033[m\n 
            Digite: \n\n 
            \033[31;107m[ 1 ]\033[m para votar na \033[36mAURORA \033[m\n 
            \033[31;107m[ 2 ]\033[m para votar na \033[34mNANA\033[m\n 
            \033[31;107m[ 3 ]\033[m para votar na \033[33mWAN-WAN \033[m\n
            \033[31;107m[ 4 ]\033[m para voto \033[30;107mnulo \033[m \n 
            \033[31;107m[ 5 ]\033[m para votar em \033[30;107mbranco!\033[m\n
     ''')
    sleep(1)
#indica que números fora dos disponíveis levam a resultado branco.
    print("\033[97;41mQualquer outro numero digitado será computado como voto em branco!\033[m\n")    
    voto = input("\nDigite o número correspondente a candidata (ou \033[97;41m\"fim\"\033[m para encerrar): ")
    sleep(1)
    if voto == 'fim':
            break 
    else:
        ano_nascimento=int(input("\033[32mQual o ano do seu nascimento?\033[m"))
        verifica=autoriza_voto(ano_nascimento)
        votacao(int(voto),verifica)
    

print('\033[35mCalculando a vencedora da eleição\033[m', end='')
sleep(2)
print('\U0001F499')
print("\n           \033[32mRESULTADO \033[m\n")
print("\033[32m-\033[m"*140)
sleep(2)
temp=False # variavel recebi "False" pra ela não interferir na contagem
cont=0     #variável recebi a quantidade de votos
cont1=0    #variável recebi as vencedora
for u in range(3):
    if num[cand[u]] > cont: #se a temp modificar dentro do for, "ela muda pra sempre".
        cont = num[cand[u]] # recebi a quantidade de votos que teve e joga na cont1
        cont1 = u           # armazena a posição dentro da lista, de 0 ate 2
        temp=True           # e ela muda se der resultado positivo, caso alguma canditada ganhe.

venc=cont1
if temp:                    # mostra o resultado personalizado de cada vencedora.
    if (cand[venc] == "AURORA"):
            print(f"A Candidata Eleita foi a \U0001F499 \033[7;34;107m AURORA...\033[m com {cont} votos.\n\033[1;36m'Ouça o SOM do NEVAR'.\033[m")  
    elif (cand[venc] == "NANA"):
        print(f"A Candidata Eleita foi a \U0001F49C \033[7;34;107m NANA...\033[m com {cont} votos.\n\033[1;34m'A aventura está nos esperando'.\033[m")      
    elif (cand[venc] == "WANWAN"):
        print(f"A Candidata Eleita foi a \U0001F49B \033[7;34;107m WAN-WAN..\033[m com {cont} votos.\n\033[33m'Pra mim diversão é tudo que importa'.\033[m")          
else:
    print('''           \033[30;107mNão teve votos suficiente para eleger uma candidata!\033[m''') #se tiver só votos nulos e brancos, nenhuma candidata é eleita

# imprime a tabelinha com os votos e com a vencedora
print(f'''
    \033[97;41m┏{"━"*17}┳{"━"*9}┓\033[m
    \033[97;41m┃\033[32;40m{"NOMES":^17}\033[97;41m┃\033[32;40m{"VOTOS":^9}\033[m\033[97;41m┃\033[m
    \033[97;41m┣{"━"*17}╋{"━"*9}┫\033[m
    \033[97;41m┃\033[36;40m{"AURORA":<17}\033[m\033[97;41m┃\033[m\033[32m{num[cand[0]]:^9}\033[m\033[97;41m┃\033[m
    \033[97;41m┃\033[34;40m{"NANA":<17}\033[m\033[97;41m┃\033[m\033[32m{num[cand[1]]:^9}\033[m\033[97;41m┃\033[m
    \033[97;41m┃\033[33;40m{"WAN-WAN":<17}\033[m\033[97;41m┃\033[m\033[32m{num[cand[2]]:^9}\033[m\033[97;41m┃\033[m
    \033[97;41m┃\033[32;40m{"Votos-Nulos":<17}\033[m\033[97;41m┃\033[m\033[32m{num[cand[3]]:^9}\033[m\033[97;41m┃\033[m
    \033[97;41m┃\033[32;40m{"Votos-Brancos":<17}\033[m\033[97;41m┃\033[m\033[32m{num[cand[4]]:^9}\033[97;41m┃\033[m
    \033[97;41m┗{"━"*17}┻{"━"*9}┛\033[m
    ''')
print("\033[32m-=\033[m"*75) 