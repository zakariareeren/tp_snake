#0.2 : On sait qu'on est dans l'environnement snake parce que c'est indiqué au niveau de chaque ligne de commande du terminal entre parenthèses



from random import randint
import pygame as pg
def pair(x):
    return x%2==0

def drawboard():
    blanc=(255, 255, 255)
    for i in range(30):
        for j in range(30):
            if (pair(i) and pair(j)) or (not(pair(i)) and not(pair(j))):  #on trouve les cases qu'on va colorier
               x,y=20*i, 20*j #On retrouve les abscisses et ordonnées des points
               rect=pg.Rect(x,y,20,20)
               pg.draw.rect(screen,blanc,rect)    

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
flag=True 

while flag==True:
    clock.tick(1)

    for event in pg.event.get():
        pass

    screen.fill((0,0,0))
    drawboard()
    pg.display.update()
    if event.type==pg.QUIT:
        flag=False

pg.quit()




    
# On ne peut fermer la fenetre avec la croix parce que : dans le programme, il n'y a aucune condition qui fasse passer le booleen à False, donc il ne s'arrête jamais
# Pour arreter le programme : 


    