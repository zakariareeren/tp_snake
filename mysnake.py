#0.2 : On sait qu'on est dans l'environnement snake parce que c'est indiqué au niveau de chaque ligne de commande du terminal entre parenthèses



from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
flag=True 

while flag==True:
    clock.tick(1)

    for event in pg.event.get():
        pass
    
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    screen.fill(random_color)
    pg.display.update()
    if event.type==pg.QUIT:
        flag=False

pg.quit()

    
     



# On ne peut fermer la fenetre avec la croix parce que : dans le programme, il n'y a aucune condition qui fasse passer le booleen à False, donc il ne s'arrête jamais
# Pour arreter le programme : 

