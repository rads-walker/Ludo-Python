# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 00:38:43 2019

@author: Danilo Rafael
"""

#!/usr/bin/env python
# coding: utf-8
import pygame
import numpy as np
from random import randint



#inicializar otdos os modulos do pygame
try:
    pygame.init()
except:
    print("Não inicializou corretamente")

'''        Testes para ver se ganha xdxd               '''

'''
dice = [1, 2, 2, 2,
        5, 2, 2, 2,
        5, 3, 2, 2,
        3, 1, 2, 2,
]
'''
#jogador atual
player = 0



'''        Definicao de Variaveis               '''
# Definicao de termos[5]:
WHITE  = (255, 255, 255)
BLACK  = (0  ,  0 ,  0 )
'''
RED    = (255,48,48)
GREEN  = ( 0, 204, 0 )
BLUE   = ( 0, 51, 204)
YELLOW = (204, 204, 0)
PINK   = (255, 187, 255)

Green_b = (198, 255, 179)
Blue_b = (179, 198, 255)
Red_b = (255, 153, 194)
yellow_b = (255, 255, 128)
'''
PINK   = (255, 187, 255)
BLUE = (28, 81, 227)
RED = (252, 23, 111)
YELLOW = (255, 242, 0)
GREEN = (84, 237, 33)

Green_b = (0, 153, 51)
Blue_b = (0, 51, 153)
Red_b = (181, 6, 76)
yellow_b = (255, 204, 0)

tab_possiveis = [(193,  46),(193,  67),(193,  88),(193, 109),(193, 130),(214, 151),(235, 151),(256, 151),(277, 151),(298, 151),(319, 151),(319, 172),(319, 193),(298, 193),(277, 193),(256, 193),(235, 193),(214, 193),(193, 214),(193, 235),(193, 256),(193, 277),(193, 298),(193, 319),(172, 319),(151, 319),(151, 298),(151, 277),(151, 256),(151, 235),(151, 214),(130, 193),(109, 193),( 88, 193),( 67, 193),( 46, 193),( 25, 193),( 25, 172),( 25, 151),( 46, 151),( 67, 151),( 88, 151),(109, 151),(130, 151),(151, 130),(151, 109),(151,  88),(151,  67),(151,  46),(151,  25),(172,  25),(193,  25)]
tab_possiveis_x = [x[0] for x in tab_possiveis]
tab_possiveis_y = [x[1] for x in tab_possiveis]

pecas_jogar = [(388,277),(438,277),(483,277),(538,277)]

sair = True

move = 0

mouse = pygame.mouse.get_pos()

# qts pecas - pecas
#player = [-1,-1,-1,-1,-1]
'''[pecas fora da base,
    -1 = peca base
     * = peca ingame
    6' = peca ganha
    ]
'''
players = np.zeros((4,5), dtype=int)
#check   = [-1,-1,-1,-1,-1]
'''[peça salva,
    -1 = peca in game
     0 = peca na safe
     1 = peca salva]
'''
check   = np.zeros((4,5), dtype=int)
players.fill(-1)
check.fill(-1)
data = [(Red_b, 0, 50),
        (Green_b, 13, 11),
        (yellow_b, 26, 24),
        (Blue_b, 39, 37)]
base = [(235, 46), (235, 235), (46, 235), (46, 46)]
safe = [(172, 46), (298, 172), (172, 298), (46, 172)]

#print(data)




'''                          Definicao de Funcoes                                 '''

#Desenha o quadro do jogo
def drawBoard():
    #Pinta o fundo
    backgound.fill(WHITE)
    ##Primeiro bloco
    #Desenha as linhas do meio
    x = 40
    while x < 330:
        pygame.draw.line(backgound, BLACK, [x,19], [x, 334], 1) #line in x
        pygame.draw.line(backgound, BLACK, [19,x], [335, x], 1) #line in y
        x += 21
    #Desenha as bordas
    pygame.draw.line(backgound, BLACK, [19,19] ,[335 ,19], 1)   # linha cima
    pygame.draw.line(backgound, BLACK, [19,19] ,[19 ,334], 1)   # linha esquerda
    pygame.draw.line(backgound, BLACK, [335,19],[335,334], 1) # linha direita
    pygame.draw.line(backgound, BLACK, [19,334],[334,334], 1) # linha baixo
    #Desenha os quadrados nos cantos
    #1°
    pygame.draw.rect(backgound, Blue_b, pygame.Rect( 20,  20, 125, 125))
    pygame.draw.rect(backgound, Red_b, pygame.Rect(209,  20, 126, 125))
    pygame.draw.rect(backgound, yellow_b , pygame.Rect( 20, 209, 125, 125))
    pygame.draw.rect(backgound, Green_b   , pygame.Rect(209, 209, 126, 125))
    #Desenha as areas seguras
    SAFE = ((146, 146),(167, 146),(188, 146),(146, 167),(167, 167),(188, 167),(146, 188),(167, 188),(188, 188))
    #list comprehension
    x = [x[0] for x in SAFE]
    y = [x[1] for x in SAFE]
    k = 0
    while k < 9:
        pygame.draw.rect(backgound, PINK, pygame.Rect(x[k], y[k], 20, 20))
        k += 1
    #segundo bloco
    pygame.draw.rect(backgound, BLACK, pygame.Rect(368, 19, 200, 316), 2)
    #linhas horizontais
    pygame.draw.line(backgound, BLACK, [368,167] ,[567 ,167], 2)
    pygame.draw.line(backgound, BLACK, [368,230] ,[567 ,230], 2)
    #peças para jogar
    pygame.draw.rect(backgound, RED, pygame.Rect(388,  277, 20, 20))
    pygame.draw.rect(backgound, RED, pygame.Rect(438,  277, 20, 20))
    pygame.draw.rect(backgound, RED, pygame.Rect(483,  277, 20, 20))
    pygame.draw.rect(backgound, RED, pygame.Rect(538,  277, 20, 20))
    #AMARELO
    pygame.draw.rect(backgound, BLUE, pygame.Rect(46,   46, 10, 10))
    pygame.draw.rect(backgound, BLUE, pygame.Rect(109,  46, 10, 10))
    pygame.draw.rect(backgound, BLUE, pygame.Rect(46, 109, 10, 10))
    pygame.draw.rect(backgound, BLUE, pygame.Rect(109,  109, 10, 10))
    #vermelho
    pygame.draw.rect(backgound, RED, pygame.Rect(235,  46, 10, 10))
    pygame.draw.rect(backgound, RED, pygame.Rect(235, 109, 10, 10))
    pygame.draw.rect(backgound, RED, pygame.Rect(298, 109, 10, 10))
    pygame.draw.rect(backgound, RED, pygame.Rect(298,  46, 10, 10))
    #Amarelo
    pygame.draw.rect(backgound, YELLOW, pygame.Rect(46,  235, 10, 10))
    pygame.draw.rect(backgound, YELLOW, pygame.Rect(109, 235, 10, 10))
    pygame.draw.rect(backgound, YELLOW, pygame.Rect(46, 298, 10, 10))
    pygame.draw.rect(backgound, YELLOW, pygame.Rect(109,  298, 10, 10))
    #Verde
    pygame.draw.rect(backgound, GREEN, pygame.Rect(235,  235, 10, 10))
    pygame.draw.rect(backgound, GREEN, pygame.Rect(235, 298, 10, 10))
    pygame.draw.rect(backgound, GREEN, pygame.Rect(298, 298, 10, 10))
    pygame.draw.rect(backgound, GREEN, pygame.Rect(298,  235, 10, 10))

    #SAFE RED
    e = 0
    while e < 5:
        pygame.draw.rect(backgound, (186, 241, 255), pygame.Rect(167           , 41 + (21 * e), 20, 20))
        pygame.draw.rect(backgound, (186, 241, 255), pygame.Rect(209 + (21 * e), 167          , 20, 20))
        pygame.draw.rect(backgound, (186, 241, 255), pygame.Rect(167           , 209 + (21 * e), 20, 20))
        pygame.draw.rect(backgound, (186, 241, 255), pygame.Rect(41  + (21 * e), 167, 20, 20))

        e += 1

#funcao de texto
def text(msg, cor, pos, size):
    #Define a fonte
    fonte = pygame.font.SysFont(None,size)
    #Define texto
    texto = fonte.render(msg, False, cor)
    #Desenha
    backgound.blit(texto, pos)

#checar melhor mensagem
def checkBestmove(dice, player, players):
    if checkDown(dice):
        print("derrubou -----------------------------------------------------")
    elif (dice == 1 or dice == 6) and players[player][0] < 3:
        print ("Liberar")
        freeCowries()
    elif players[player][0] >= 0 and  players[player][0] > check[player][0]:
        print("mover")
        freeMove(dice, player, players)
    print(players)

#Liberar peça
def freeCowries():
    players[player][0] += 1
    e = 1
    while e < 5:
        if players[player][e] == -1:
            #peca que vai ser liberada recebe o valor correspondente ao 0 da sua co
            players[player][e] = data[player][1]
            #Se for o jogador pinte
            if player == 0:
                paint(GREEN, [pecas_jogar[e-1][0], pecas_jogar[e-1][1]], [20, 20], 0)
            paint_release(e)
            return e
        e += 1


def checkSafe():
    #verificar na lista check se existe 0 = alguma peca na safe
    if 0 in check[player][1:]:
        #pegar a posicao dela
        e, = np.where(check[player][1:] == 0)
        #retornar a primeira posicao
        #correcao para valor 0 qe e == false
        e[0] += 1
        return e
    else:
        return False

def checkLast(pos):
    #verificar na lista se tem alguma peca na ultima posicao
    if pos in players[player][1:]:
        #pegar a posicao dela
        e, = np.where(players[player][1:] == pos)
        #retornar a primeira
        #correcao para valor 0 qe e == false
        e[0] += 1
        #print (e)
        return e[0]
    else:
        return False

def checkBest():
    #Ver o mais mais perto do fim
    maxi = -1
    pos = 0
    e = 1
    while e < 5:
        if check[player][e] == -1:
            if player == 0:
                aux = players[player][e]
            else:
                #maior que 0 e menor que a posicao final
                if -1 < players[player][e] <= data[player][2]:
                    # estrapolou o fim do player, então tem que haver a correcao de 51 + 1, considerando o 0 + pos da peca
                    aux = players[player][e] + 51 + 1
                else:
                    aux = players[player][e]
            if aux > maxi:
                #print (aux, maxi)
                maxi = aux
                pos = e
        e += 1
    return pos

def freeMove(dice, player, players):
    #se tem peca na safe retorna ela
    checksafe = checkSafe()
    #se esta na ultima posicao e tira 6 == win
    checklast = checkLast(data[player][2])
    #peca mais distante que n esta na safe -- posicao
    peca = checkBest()
    #print ("checksafe", "checklast", "peca")
    #print ("  ",checksafe,"  ", checklast, "  ", peca)
    #se jog != 0 correca nas pos
    if player != 0:
        #fim corrigem em 51 + 1, 51 e o 0
        data_fim = data[player][2] + 51 + 1
        if (data[player][1] - 1) < players[player][peca] < 52:
             pos_peca = players[player][peca]
        else:
            # estrapolou o fim do player, então tem que haver a correcao de 51 + 1, considerando o 0
            pos_peca = players[player][peca] + 51 + 1
    else:
        data_fim = data[player][2]
        pos_peca = players[player][peca]
    #print (players[player][peca])

    #mover safe
    if checksafe:
        #print ("Peca na safe")
        #corrigir posicao
        if player == 0:
            #pinta da cor safe
            paint((186, 241, 255), [safe[player][0] , safe[player][1] + (players[player][checksafe] * 21) ] ,[10, 10], 0)
            #print (players[player][checksafe])
            #ganhou safe
            if dice + players[player][checksafe] >= 5:
                #print("deu")
                #posicao de peca salva
                paint(data[player][0], [safe[player][0], safe[player][1] + (5 * 21)] ,[10, 10], 0)
                check[player][0] += 1
                check[player][checksafe] = 1
                players[player][checksafe] = -2
            else:
                #print("Ndeu")
                paint(data[player][0], [safe[player][0] , safe[player][1] + ((players[player][checksafe] + dice) * 21) ] ,[10, 10], 0)
                players[player][checksafe] += dice

        if player == 1:
            #pinta da cor safe
            paint((186, 241, 255), [safe[player][0] - (players[player][checksafe] * 21) , safe[player][1]] ,[10, 10], 0)
            #print (players[player][checksafe])
            #ganhou safe
            if dice + players[player][checksafe] >= 5:
                #print("deu")
                #posicao de peca salva
                paint(data[player][0], [safe[player][0] - (5 * 21), safe[player][1]], [10, 10], 0)
                check[player][0] += 1
                check[player][checksafe] = 1
                players[player][checksafe] = -2
            else:
                #print("Ndeu")
                paint(RED, [safe[player][0] - ((players[player][checksafe] + dice) * 21)  , safe[player][1]] ,[10, 10], 0)
                players[player][checksafe] += dice

        if player == 2:
            #pinta da cor safe
            paint((186, 241, 255), [safe[player][0], safe[player][1] - (players[player][checksafe] * 21)] ,[10, 10], 0)
            #print (players[player][checksafe])
            #ganhou safe
            if dice + players[player][checksafe] >= 5:
                #print("deu")
                #posicao de peca salva
                paint(data[player][0], [safe[player][0], safe[player][1] - (5 * 21)], [10, 10], 0)
                check[player][0] += 1
                check[player][checksafe] = 1
                players[player][checksafe] = -2
            else:
                #print("Ndeu")
                paint(RED, [safe[player][0], safe[player][1] - ((players[player][checksafe] + dice) * 21)] ,[10, 10], 0)
                players[player][checksafe] += dice

        if player == 3:
            #pinta da cor safe
            paint((186, 241, 255), [safe[player][0] + (players[player][checksafe] * 21) , safe[player][1]] ,[10, 10], 0)
            #print (players[player][checksafe])
            #ganhou safe
            if dice + players[player][checksafe] >= 5:
                #print("deu")
                #posicao de peca salva
                paint(data[player][0], [safe[player][0] + (5 * 21), safe[player][1]], [10, 10], 0)
                check[player][0] += 1
                check[player][checksafe] = 1
                players[player][checksafe] = -2
            else:
                #print("Ndeu")
                paint(RED, [safe[player][0] + ((players[player][checksafe] + dice) * 21)  , safe[player][1]] ,[10, 10], 0)
                players[player][checksafe] += dice



    #se esta na ultima posicao e tira 6 == win
    elif checklast and dice == 6:
        #print ("Ultima posicao")
        if player == 0:
            paint(WHITE, [tab_possiveis[players[player][checklast]][0], tab_possiveis[players[player][checklast]][1]] ,[10, 10], 1)
            paint(RED, [172, 151] ,[10, 10], 0)
            check[player][0] += 1
            check[player][checklast] = 1
            players[player][peca] = -2

        if player == 1:
            paint(WHITE, [tab_possiveis[players[player][checklast]][0], tab_possiveis[players[player][checklast]][1]] ,[10, 10], 1)
            paint(data[player][0], [safe[player][0] - (5 * 21), safe[player][1]], [10, 10], 0)
            check[player][0] += 1
            check[player][checklast] = 1
            players[player][peca] = -2

        if player == 2:
            paint(WHITE, [tab_possiveis[players[player][checklast]][0], tab_possiveis[players[player][checklast]][1]] ,[10, 10], 1)
            paint(data[player][0], [safe[player][0], safe[player][1] - (5 * 21)], [10, 10], 0)
            check[player][0] += 1
            check[player][checklast] = 1
            players[player][peca] = -2

        if player == 3:
            paint(WHITE, [tab_possiveis[players[player][checklast]][0], tab_possiveis[players[player][checklast]][1]] ,[10, 10], 1)
            paint(data[player][0], [safe[player][0] + (5 * 21), safe[player][1]], [10, 10], 0)
            check[player][0] += 1
            check[player][checklast] = 1
            players[player][peca] = -2



    #se jogador na pos atual (com correcao) + dado > fim
    elif (pos_peca + dice) > data_fim:
        #print ("Posicao + Dado > fim")
        #rest recebe a diferenca entre o final e a pos + dice - correcao para vetor
        rest = (players[player][peca] + dice) - data[player][2] - 1
        paint(WHITE, [tab_possiveis_x[players[player][peca]], tab_possiveis_y[players[player][peca]]] ,[10, 10], 1)

        if player == 0:
            check[player][peca] = 0
            paint(data[player][0], [safe[player][0], safe[player][1] + (rest * 21)] ,[10, 10], 0)
            players[player][peca] = rest
            #print (check)
        elif player == 1:
            check[player][peca] = 0
            paint(data[player][0], [safe[player][0] - (rest * 21), safe[player][1]] ,[10, 10], 0)
            players[player][peca] = rest
            #print (check)
        elif player == 2:
            check[player][peca] = 0
            paint(data[player][0], [safe[player][0], safe[player][1]  - (rest * 21)] ,[10, 10], 0)
            players[player][peca] = rest
            #print (check)
        elif player == 3:
            check[player][peca] = 0
            paint(data[player][0], [safe[player][0] + (rest * 21), safe[player][1]] ,[10, 10], 0)
            players[player][peca] = rest
            #print (check)

    #mover livremente pelo tabuleiro
    else:
        #print("mover")
        paint(WHITE,[tab_possiveis[players[player][peca]][0], tab_possiveis[players[player][peca]][1]], [10, 10], 1)
        #paint(WHITE, [tab_possiveis[players[player][pos_peca]][0], tab_possiveis[players[player][pos_peca]][1]], [10, 10], 1)
        if player != 0:
            if pos_peca + dice > 51:
                rest = pos_peca + dice - 52
            else:
                rest = pos_peca + dice
        else:
            rest = players[player][peca] + dice

        paint(data[player][0], [tab_possiveis[rest][0], tab_possiveis[rest][1]] ,[10, 10], 0)
        #paint(RED, [tab_possiveis_x[players[player][peca] + dice], tab_possiveis_y[players[player][peca] + dice]] ,[10, 10], 0)
        players[player][peca] = rest

#pintar de cor uma posição com um tamanho, verificando se e para apagar uma pos, verificação de sobreposição de peças
#sob - 0 não tem sobreposicao
#sob - 1 possivel ter sobreposicao
def paint(color, pos, tam, sob):
    #se existe possibilidade de peça na pos que vai pintar de branco
    if sob == 1 and color == WHITE:
        #pega o index com base na posicao
        e = tab_possiveis.index((pos[0], pos[1]))
        #mais de uma peca na pos
        if sum(players[player][1:] == e) > 1:
            pygame.draw.rect(backgound, data[player][0], [pos[0], pos[1], tam[0], tam[1]])
            return True
        # jogdor sai da base de outro
        # jogador sai da base mas tem outra peca naquela pos
        # verifica se pos e uma final
        if e in [x[1] for x in data]:
            #pega index do da pos final == qual jogador tem o fim
            i = [x[1] for x in data].index(e)
            #verificar se alguem tem peca nessa pos
            player_t = 0
            while player_t < 4:
                #jogador tem qe ser diferentes
                if player != player_t:
                    #verificar se alguem tem peca nessa pos
                    print(player_t, i, e, players[player_t][1:])
                    if i in players[player_t][1:]:
                        pygame.draw.rect(backgound, data[player_t][0], [pos[0], pos[1], tam[0], tam[1]])
                        return True
                player_t += 1
    pygame.draw.rect(backgound, color, [pos[0], pos[1], tam[0], tam[1]])

#pintar peca da base quando libera uma peça
def paint_release(e):
    ex = 0
    ey = 0
    #verifica se ta na base ou pos bas da cor
    if players[player][e] == data[player][1]:
        if (e-1) == 1:
            ex += 63
        elif (e-1) == 2:
            ey += 63
        elif (e-1) == 3:
            ex += 63
            ey =+ 63
        #pinta a cor correspondente na base e pinta na primeira pos
        paint(WHITE, [base[player][0] + ex, base[player][1]  + ey], [10, 10], 0)
        paint(data[player][0], [tab_possiveis_x[data[player][1]], tab_possiveis_y[data[player][1]]], [10, 10], 0)

#pintar peca da base quando bloquear uma peça
def paint_lock(player, pos):
    aux_x = 0
    aux_y = 0
    pos -= 1
    if   pos == 1:
        aux_x += 63
    elif pos == 2:
        aux_y += 63
    elif pos == 3:
        aux_x += 63
        aux_y =+ 63
    paint(data[player][0], [base[player][0] + aux_x, base[player][1]  + aux_y], [10, 10], 0)



def checkWin(isWin):
    if isWin == 3:
        return True
    else:
        return False

def checkDown(dice):
    #Mover normalmente no tabuleiro e encontra uma peça de outro jogador -> derruba essa peça
    #Pode ter uma peça de outro jogador na 1° posição de quando for liberar uma sua -> derruba tirando 1 ou 6
    #Levar em conta tmb que se tiver duas ou mais peças daquele jogador naquela posição tem que derrubar todas

    #peca de teste do jogador atual
    e = 1
    while e < 5:
        #peca +  dado == nova posicao
        new_pos = players[player][e] + dice
        #se estrapolar 51, recebe - 52, correcao do zero e da pos no tabuleiro
        if new_pos > 51:
            new_pos -= 52

        # o check for diferente de ingame ou nova posicao for uma pos[0] de outro jogador ou a new_pos for maior que o fim do jogador
        if check[player][e] != -1 or new_pos > data[player][2]:
            e += 1
        else:
            #liberar peca derrubar outras
            #verifica a pos da peca e a da base e se tem 6 ou 1 no dado
            if players[player][e] == -1 and (dice == 1 or dice == 6):

                fim_p = data[player][1]
                #ver se tem alguma outra peca nessa pos
                player_t = 0
                while player_t < 4:
                    if player != player_t:
                        #existe ao menos uma peca de um jogador naquela pos
                        if fim_p in players[player_t][1:]:
                            print ("Ao Liberar")
                            #ver quantas tem
                            total_p = sum(players[player_t][1:] == fim_p)
                            pecas = 1
                            while pecas <= total_p:
                                #procura para pegar o indece no vetor de jogadores qual peca que ta na base do jogador atual
                                pos = [x for x in players[player_t][1:]].index(data[player][1])
                                #correcao pos 0 do vetor
                                pos += 1
                                #Libera a peca
                                freeCowries()
                                #loca a peca do jogador alvo
                                #print (player_t, pos + 1)
                                paint_lock(player_t, pos + 1)
                                #peca do jog alvo vai base
                                players[player_t][pos] = -1
                                #jogador alvo recebe -1 peca em jogo
                                players[player_t][0] -= 1
                                #prox peca de tiver mais de uma
                                pecas += 1
                            return True
                    player_t += 1

            if players[player][e] != -1:

                #verifica peca + dado se derruba
                player_t = 0
                while player_t < 4:
                    #se o jogador for o que vai ser testado pula
                    if player != player_t:
                            #existe ao menos uma peca de um jogador naquela pos
                            if new_pos in players[player_t][1:]:
                                print("Ao andar")
                                #ver quantas tem
                                total_p = sum(players[player_t][1:] == new_pos)
                                #pega as pos no vetor
                                pos_t = np.where(players[player_t][1:] == new_pos)
                                pecas_t = 1
                                print("player_t = ", player_t)
                                print("new_pos = ", new_pos)
                                print("pos_t = ", pos_t)
                                print("total_p = ", total_p)

                                while pecas_t <= total_p:
                                    #se a peca esta em jogo ou seja check == -1
                                    #checa o player teste na pos[0] ou seja numeros [0][i-1] para correcao de uso de vetor
                                    if check[player_t][pos_t[0][pecas_t-1]] == -1:
                                        #derruba
                                        #branco a pos da peca anterior ao mover
                                        paint(WHITE, [tab_possiveis[players[player][e]][0], tab_possiveis[players[player][e]][1]], [10, 10], 0)
                                        #pinto a nova pos dela
                                        paint(data[player][0], [tab_possiveis[new_pos][0], tab_possiveis[new_pos][1]], [10, 10], 0)
                                        #passa a por corrigindo do vet
                                        #print (player_t, pos_t[0][pecas_t-1] + 1)
                                        paint_lock(player_t, (pos_t[0][pecas_t-1] + 1))
                                        #peca volta para base
                                        players[player_t][(pos_t[0][pecas_t-1] + 1)] = -1
                                        #jogador diminui peca in game
                                        players[player_t][0] -= 1
                                        #peca que derrubou vai pra nova pos
                                        players[player][e] = new_pos
                                    pecas_t += 1
                                return True
                    player_t +=1
            e += 1


    return False

def checkPlayer (dice, player):
    if dice != 6:
        player += 1
        if player == 4:
            player = 0
    return player


#Initialize the Windows
backgound = pygame.display.set_mode((600,380))
#Set the Name
pygame.display.set_caption("Ludo")
#Draw the Board
drawBoard()

#teste dado
#cont = 0
while sair:
    mouse = pygame.mouse.get_pos()
    #print(mouse)
    #Jogador
    #if player == 0:
#        text("DADO", BLACK, [370, 169], 95)
    #Maquina
    #else:
    text("NEXT", BLACK, [379, 169], 95)

    for event in pygame.event.get():
        #print(event)
        #posicao do botao na tela
        if  567 > mouse[0] > 370 and 230 > mouse[1] > 169:
            #verificar clique na tela
            if event.type == pygame.MOUSEBUTTONDOWN:

                #respota ao clique
#                paint(RED,[370,169],[197,61], 0)
                #apagar numero do dado anterior
                paint(WHITE,[370,21],[197,146], 0)
                #Rolar o dado
                dice = randint(1,6)

                print("Jogador:", player + 1, "dado:", dice)
                #imprimir dado na tela

#                checkBestmove(dice[cont], player, players)
                checkBestmove(dice, player, players)

                #valor do dado
                #text(str(dice[cont]), BLACK,  [453,65], 100)
                text(str(dice), BLACK,  [453,65], 100)

                player = checkPlayer(dice, player)
                #player = checkPlayer(dice[cont], player)

                #proximo numero do vet dado
                #cont += 1
                if checkWin(check[player][0]):
                    print("GANHOUs")



        #quit the game
        if event.type == pygame.QUIT:
            sair = False
    #atualizar a tela
    pygame.display.update()



pygame.quit()
