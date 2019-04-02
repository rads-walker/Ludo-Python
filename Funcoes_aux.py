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




    e = 1
    while e < 5:
#        print ("peca test", players[player][e], "pos ", e)
        #new_pos = posicao + dado
        new_pos = players[player][e] + dice
        if new_pos > 51:
            new_pos -= 52
        #print("NEW POS", new_pos)
        # o check for diferente de ingame ou nova posicao for uma pos[0] de outro jogador ou a new_pos for maior que o fim do jogador
        if check[player][e] != -1 or new_pos in [x[1] for x in data] or new_pos > data[player][2]:
            e += 1

        else:
            player_t = 0
            while player_t < 4:
                #se o jogador for o que vai ser testado pula
                if player != player_t:
                    #verifica se ao liberar derrubou alguma peca
                    #se ela estiver na base == -1
                    if players[player][e] == -1 and (dice == 1 or dice == 6):
                        #se a pos inicial for a pos de uma peca de outro jogador
                        if data[player][1] in players[player_t][1:]:
                            pos = [x for x in players[player_t][1:]].index(data[player][1]) + 1
                            verificar checagem de pos
                            #Libera a peca
                            freeCowries()
                            #loca a peca do jogador alvo
                            paint_lock(player_t, pos)
                            #peca do jog alvo vai base
                            players[player_t][pos] = -1
                            #jogador alvo recebe -1 peca em jogo
                            players[player_t][0] -= 1
                            return True
                        
                    peca_t = 1
                    #testa as 4 pecas
                    while peca_t < 5: 
                        #players[player_t][peca_t]
                        #ela esta em jogo ou seja check == -1
                        if check[player_t][peca_t] == -1:
                            #se a new_pos for igual a pos de um peca de um jogador
                            if new_pos == players[player_t][peca_t]:
                                #pintar pos antiga de branco
                                paint(WHITE, [tab_possiveis[players[player][e]][0], tab_possiveis[players[player][e]][1]], [10, 10], 0)
                                paint(data[player][0], [tab_possiveis[new_pos][0], tab_possiveis[new_pos][1]], [10, 10], 0)
                                paint_lock(player_t, peca_t)   
                                #peca volta para base
                                players[player_t][peca_t] = -1
                                #jogador diminui peca in game
                                players[player_t][0]    -= 1
                                #peca que derrubou vai pra nova pos
                                players[player][e] = new_pos
                                return True
                        peca_t += 1
                player_t += 1                    
        e += 1