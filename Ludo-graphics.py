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



'''        Definicao de Variaveis               '''
# Definicao de termos[5]:
WHITE  = (255, 255, 255)
BLACK  = (0  ,  0 ,  0 )
RED    = (255,48,48)
GREEN  = ( 0 , 255,  0 )
BLUE   = ( 187 ,  255 , 255)
YELLOW = (255, 255,  0 )
PINK   = (255, 187, 255)

tab_possiveis = [(193,  46),(193,  67),(193,  88),(193, 109),(193, 130),(214, 151),(235, 151),(256, 151),(277, 151),(298, 151),(319, 151),(319, 172),(319, 193),(298, 193),(277, 193),(256, 193),(235, 193),(214, 193),(193, 214),(193, 235),(193, 256),(193, 277),(193, 298),(193, 319),(172, 319),(151, 319),(151, 298),(151, 277),(151, 256),(151, 235),(151, 214),(130, 193),(109, 193),( 88, 193),( 67, 193),( 46, 193),( 25, 193),( 25, 172),( 25, 151),( 46, 151),( 67, 151),( 88, 151),(109, 151),(130, 151),(151, 130),(151, 109),(151,  88),(151,  67),(151,  46),(151,  25),(172,  25),(193,  25)]
tab_possiveis_x = [x[0] for x in tab_possiveis]
tab_possiveis_y = [x[1] for x in tab_possiveis]

pecas_jogar = [(388,277),(438,277),(483,277),(538,277)]
pos_red = [(172, 46)]
pos_green = [(235,46),(235,109),(298,109),(298,46)]



sair = True

move = 0

mouse = pygame.mouse.get_pos()

# qts pecas - pecas
#player = [-1,-1,-1,-1,-1]
players = np.zeros((4,5), dtype=int)
players.fill(-1)
data = [(RED, 0, 50),(GREEN, 13, 11),(YELLOW, 26, 24),(BLUE, 35, 33)]
base = [(235, 46), (235, 235), (46, 235), (46, 46)]
safe = [(172, 46), (214, 172), (172, 214), (25, 172)]

print(data)

tabuleiro = np.zeros((54), dtype=int)
#jogador atual
player = 0




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
    pygame.draw.rect(backgound, YELLOW, pygame.Rect( 20,  20, 125, 125))
    pygame.draw.rect(backgound, BLUE  , pygame.Rect(209,  20, 126, 125))
    pygame.draw.rect(backgound, GREEN , pygame.Rect( 20, 209, 125, 125))
    pygame.draw.rect(backgound, RED   , pygame.Rect(209, 209, 126, 125))
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
    pygame.draw.rect(backgound, RED, pygame.Rect(46,   46, 10, 10))
    pygame.draw.rect(backgound, RED, pygame.Rect(109,  46, 10, 10))
    pygame.draw.rect(backgound, RED, pygame.Rect(46, 109, 10, 10))
    pygame.draw.rect(backgound, RED, pygame.Rect(109,  109, 10, 10))
    #vermelho
    pygame.draw.rect(backgound, RED, pygame.Rect(235,  46, 10, 10))
    pygame.draw.rect(backgound, RED, pygame.Rect(235, 109, 10, 10))
    pygame.draw.rect(backgound, RED, pygame.Rect(298, 109, 10, 10))
    pygame.draw.rect(backgound, RED, pygame.Rect(298,  46, 10, 10))
    #VERDE
    pygame.draw.rect(backgound, RED, pygame.Rect(46,  235, 10, 10))
    pygame.draw.rect(backgound, RED, pygame.Rect(109, 235, 10, 10))
    pygame.draw.rect(backgound, RED, pygame.Rect(46, 298, 10, 10))
    pygame.draw.rect(backgound, RED, pygame.Rect(109,  298, 10, 10))
    #AZUL
    pygame.draw.rect(backgound, BLUE, pygame.Rect(235,  235, 10, 10))
    pygame.draw.rect(backgound, BLUE, pygame.Rect(235, 298, 10, 10))
    pygame.draw.rect(backgound, BLUE, pygame.Rect(298, 298, 10, 10))
    pygame.draw.rect(backgound, BLUE, pygame.Rect(298,  235, 10, 10))

#funcao de texto
def text(msg, cor, pos, size):
    #Define a fonte
    fonte = pygame.font.SysFont(None,size)    
    #Define texto
    texto = fonte.render(msg, False, cor)
    #Desenha
    backgound.blit(texto, pos)

#checar melhor mensagem
def checkBestmove(dice, player, players, tabuleiro):
    if downCowries(dice, player, players, tabuleiro):
        print("derrubar")
    elif (dice == 1 or dice == 6) and players[player,0] < 3:
        print ("Liberar")
        e = freeCowries(dice, players[player][:], tabuleiro)
        paint_release(players[player][e], e)
        return True
    elif players[player,0] >= 0:
        freeMove(dice, player, players)
        print("mover")

#Liberar peça        
def freeCowries(dice, players, tabuleiro):  
    players[0] += 1
    e = 1
    while e < 5:
        if players[e] == -1:
            players[e] = 0
            break
        e += 1    
    paint(GREEN, [pecas_jogar[e-1][0], pecas_jogar[e-1][1]], [20, 20])
    return e    


        
def freeMove(dice, player, players):
    e = np.argmax(players[player][1:])+1
    paint(WHITE, [tab_possiveis_x[players[player][e]], tab_possiveis_y[players[player][e]]] ,[10, 10])
    #se jogador na pos atual + dado > fim
    if (players[player][e] + dice) > data[player][2]:
        #rest recebe a diferenca entre o final e a pos + dice
        rest = players[player][e] + dice - data[player][2]

        if player == 0:
            
            paint(RED, [safe[player][0], safe[player][0] + ((rest - 1) * 21)], [10, 10])
            players[player][e] = -106 - rest
        elif player == 1:
            ex += 63
        elif player == 2:
            ey += 63
        elif player == 3:
            ex += 63
            ey =+ 63
        paint(RED, [safe[player]
        tab_possiveis_x[players[player][e] + dice], tab_possiveis_y[players[player][e] + dice]] ,[10, 10])
    else:
        paint(RED, [tab_possiveis_x[players[player][e] + dice], tab_possiveis_y[players[player][e] + dice]] ,[10, 10])
        players[player][e] += dice
    #mais de uma peca na 1° casa
    if data[player][1] in players[player][1:]:
        paint(data[player][0], [tab_possiveis_x[data[player][1]], tab_possiveis_y[data[player][1]]], [10, 10])
    
def downCowries(dice, x, jogadores, tabuleiro):
    return False

#pintar de cor uma posição com um tamanho
def paint(color, pos, tam):
    pygame.draw.rect(backgound, color, [pos[0], pos[1], tam[0], tam[1]])

def paint_release(peca, e):
    ex = 0
    ey = 0
    if peca == 0:
        if (e-1) == 1:
            ex += 63
        elif (e-1) == 2:
            ey += 63
        elif (e-1) == 3:
            ex += 63
            ey =+ 63
        paint(WHITE, [base[player][0] + ex, base[player][1]  + ey], [10, 10])
        paint(data[player][0], [tab_possiveis_x[data[player][1]], tab_possiveis_y[data[player][1]]], [10, 10])

    #set(tabuleiro)
    
#Initialize the Windows
backgound = pygame.display.set_mode((600,380))
#Set the Name
pygame.display.set_caption("Ludo")
#Draw the Board
drawBoard()






while sair:
    mouse = pygame.mouse.get_pos()
    #print(mouse)
    text("DADO", BLACK, [370, 169], 95)

    for event in pygame.event.get():
        #print(event)
        #posicao do botao na tela
        if  567 > mouse[0] > 370 and 230 > mouse[1] > 169:
            #verificar clique na tela
            if event.type == pygame.MOUSEBUTTONDOWN:
                #respota ao clique
                paint(RED,[370,169],[197,61])           
                #Rolar o dado
                dice = randint(1,6)       
                #apagar numero do dado anterior
                paint(WHITE,[370,21],[197,146])
                #imprimir texto na tela
                text(str(dice), BLACK,  [453,65], 100)
                 
                checkBestmove(dice, player, players, tabuleiro)
                
#                #apagar a peça
#                pygame.draw.rect(backgound, WHITE, [ x[move], y[move], 10, 10])
#
#               move += dice
#                #if move < 51:
#                    #pygame.draw.rect(backgound,  RED , [ x[move] ,  y[move] , 10, 10])
#                #else:
#                    #move -= 51
#                    #pygame.draw.rect(backgound,  RED , [ x[move] ,  y[move] , 10, 10])
#
#                print(dice,move)


        #quit the game
        if event.type == pygame.QUIT:
            sair = False
    #atualizar a tela
    pygame.display.update()


pygame.quit()
