import pygame
import numpy as np

#definition of terms
WHITE  = (255, 255, 255)
BLACK  = (0  ,  0 ,  0 )
RED    = (255,48,48)
GREEN  = ( 0 , 255,  0 )
BLUE   = ( 187 ,  255 , 255)
YELLOW = (255, 255,  0 )
PINK   = (255, 187, 255)



def getPos():
    s = (15,15)
    vet_pinta = np.zeros((15,15),dtype='i,i')
    vet_pos   = np.zeros((15,15),dtype='i,i')
    c = 0
    l = 0
    while c < 15:
        l = 0
        while l < 15:
            x  = 20+(l*20+l)
            x1 = 25+(l*20+l)
            y  = 20+(c*20+c)
            y1 = 25+(c*20+c)
            vet_pinta[l,c] = (y,x)
            vet_pos[l,c] = (y1,x1)
            pygame.draw.rect(backgound, player, pygame.Rect(x , y , 20, 20))
            pygame.draw.rect(backgound,  RED  , pygame.Rect(x1, y1, 10, 10))
            l += 1
        c += 1
    print(vet_pinta)
    print(vet_pos)

def drawBoard():
    backgound.fill(WHITE)    
    #middle
    x = 40
    while x < 330:
        pygame.draw.line(backgound, BLACK, [x,19], [x, 334], 1) #line in x
        pygame.draw.line(backgound, BLACK, [19,x], [335, x], 1) #line in y
        x += 21
    #borders
    pygame.draw.line(backgound, BLACK, [19,19] ,[335 ,19], 1)   # linha cima
    pygame.draw.line(backgound, BLACK, [19,19] ,[19 ,334], 1)   # linha esquerda
    pygame.draw.line(backgound, BLACK, [335,19],[335,334], 1) # linha direita
    pygame.draw.line(backgound, BLACK, [19,334],[334,334], 1) # linha baixo
    #color rest
    pygame.draw.rect(backgound, YELLOW, pygame.Rect( 20,  20, 125, 125))
    pygame.draw.rect(backgound, BLUE  , pygame.Rect(209,  20, 126, 125))
    pygame.draw.rect(backgound, GREEN , pygame.Rect( 20, 209, 125, 125))
    pygame.draw.rect(backgound, RED   , pygame.Rect(209, 209, 126, 125))
    #color safe
    SAFE = ((146, 146),(167, 146),(188, 146),(146, 167),(167, 167),(188, 167),(146, 188),(167, 188),(188, 188))
    x = [x[0] for x in SAFE]
    y = [x[1] for x in SAFE]
    k = 0
    while k < 9:
        pygame.draw.rect(backgound, PINK, pygame.Rect(x[k], y[k], 20, 20))
        k += 1
            





'''
Test fill and player
pygame.draw.rect(backgound, PINK, pygame.Rect(146, 20, 20, 20))
pygame.draw.rect(backgound, RED,    pygame.Rect(151, 25, 10, 10))

'''





try:
    pygame.init()
except:
    print("Não inicializou corretamente")
    
#Initialize the Windows
backgound = pygame.display.set_mode((400,400))
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
pygame.draw.rect(backgound, RED, pygame.Rect(193,  46, 10, 10))
move = 0

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print(event)
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