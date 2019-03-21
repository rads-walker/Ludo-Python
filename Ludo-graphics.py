import pygame
import numpy as np
from random import randint


#inicializar otdos os modulos do pygame
#para especificos usar
try:
    pygame.init()
except:
    print("Não inicializou corretamente")



#Definicao de termos
WHITE  = (255, 255, 255)
BLACK  = (0  ,  0 ,  0 )
RED    = (255,48,48)
GREEN  = ( 0 , 255,  0 )
BLUE   = ( 187 ,  255 , 255)
YELLOW = (255, 255,  0 )
PINK   = (255, 187, 255)

#Recupera as posicoes x e y da matriz desenhada na tela
def getPos():
    #Vetor de posicoes para desenha todo o quadrado da malha
    vet_pinta = np.zeros((15,15),dtype='i,i')
    #Vetor de posicoes para desenha a peça na malha
    vet_pos   = np.zeros((15,15),dtype='i,i')
    c = 0
    l = 0
    #Loop em todas as posicoes
    while c < 15:
        l = 0
        while l < 15:
            x  = 20+(l*20+l)
            x1 = 25+(l*20+l)
            y  = 20+(c*20+c)
            y1 = 25+(c*20+c)
            vet_pinta[l,c] = (y,x)
            vet_pos[l,c] = (y1,x1)
            #Desenha na tela
            pygame.draw.rect(backgound, (218, 165, 32), pygame.Rect(x , y , 20, 20))
            pygame.draw.rect(backgound,  RED  , pygame.Rect(x1, y1, 10, 10))
            l += 1
        c += 1
        
def freeCowries(dice, x, jogadores, tabuleiro):
    if(dice == 1 or dice == 6) and (jogadores[x,0] < 3):
        jogadores[x,0] += 1
        return True
    return False


#funcao de texto
def text(msg, cor, pos, size):
    #Define a fonte
    fonte = pygame.font.SysFont(None,size)    
    #Define texto
    texto = fonte.render(msg, False, cor)
    #Desenha
    backgound.blit(texto, pos)

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
    #peças possiveis
    pygame.draw.rect(backgound, RED, pygame.Rect(388,  277, 20, 20))
    pygame.draw.rect(backgound, RED, pygame.Rect(438,  277, 20, 20))
    pygame.draw.rect(backgound, RED, pygame.Rect(483,  277, 20, 20))
    pygame.draw.rect(backgound, RED, pygame.Rect(538,  277, 20, 20))

    #AMARELO
    pygame.draw.rect(backgound, RED, pygame.Rect(46,   46, 10, 10))
    pygame.draw.rect(backgound, RED, pygame.Rect(109,  46, 10, 10))
    pygame.draw.rect(backgound, RED, pygame.Rect(46, 109, 10, 10))
    pygame.draw.rect(backgound, RED, pygame.Rect(109,  109, 10, 10))
    
    #AZUL
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
    
#Initialize the Windows
backgound = pygame.display.set_mode((600,380))
#Set the Name
pygame.display.set_caption("Ludo")
sair = True
#Draw the Board
drawBoard()

test_pos = [(193,  46),(193,  67),(193,  88),(193, 109),(193, 130),(214, 151),(235, 151),(256, 151),(277, 151),(298, 151),(319, 151),(319, 172),(319, 193),(298, 193),(277, 193),(256, 193),(235, 193),(214, 193),(193, 214),(193, 235),(193, 256),(193, 277),(193, 298),(193, 319),(172, 319),(151, 319),(151, 298),(151, 277),(151, 256),(151, 235),(151, 214),(130, 193),(109, 193),( 88, 193),( 67, 193),( 46, 193),( 25, 193),( 25, 172),( 25, 151),( 46, 151),( 67, 151),( 88, 151),(109, 151),(130, 151),(151, 130),(151, 109),(151,  88),(151,  67),(151,  46),(151,  25),(172,  25),(193,  25)]
x = [x[0] for x in test_pos]
y = [x[1] for x in test_pos]
#print(x)
#print(y)


move = 0

mouse = pygame.mouse.get_pos()
print(mouse)

while sair:
    mouse = pygame.mouse.get_pos()
    #print(mouse)
    text("DADO", BLACK, [370, 169], 95)

    for event in pygame.event.get():
        #print(event)
        if  567 > mouse[0] > 370 and 230 > mouse[1] > 169:
            #pygame.draw.rect(backgound, GREEN, (370, 169, 197, 61))
            if event.type == pygame.MOUSEBUTTONDOWN:
                #respota ao clique
                pygame.draw.rect(backgound, RED, (370, 169, 197, 61))
                dice = randint(1,6)
                #apagar numero
                pygame.draw.rect(backgound, WHITE, pygame.Rect(370, 21, 197, 146))
                
                #imprimir texto na tela
                text(str(dice), BLACK,  [453,65], 100)
                
                #apagar a peça
                pygame.draw.rect(backgound, WHITE, [ x[move], y[move], 10, 10])

                move += dice
                if move < 51:
                    pygame.draw.rect(backgound,  RED , [ x[move] ,  y[move] , 10, 10])
                else:
                    move -= 51
                    pygame.draw.rect(backgound,  RED , [ x[move] ,  y[move] , 10, 10])

                print(dice,move)
            else:
                pygame.draw.rect(backgound, (244,244,244), (370, 169, 197, 61))

        if event.type == pygame.QUIT:
            sair = False
        if event.type == pygame.KEYDOWN:
            #print(event)
            if event.key == pygame.K_LEFT:
                if move < 51:
                    move += 1
                    pygame.draw.rect(backgound, WHITE, [  x[51]  ,   y[51]  , 10, 10])
                    pygame.draw.rect(backgound, WHITE, [x[move-1], y[move-1], 10, 10])
                    pygame.draw.rect(backgound,  RED , [ x[move] ,  y[move] , 10, 10])
                else:
                    pygame.draw.rect(backgound, WHITE, [  x[51]  ,   y[51]  , 10, 10])
                    move = 0
                    pygame.draw.rect(backgound,  RED , [ x[move] ,  y[move] , 10, 10])
    pygame.display.update()


pygame.quit()
