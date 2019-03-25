# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 20:51:45 2019

@author: danil
"""
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
