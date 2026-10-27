#0.2 : On sait qu'on est dans l'environnement snake parce que c'est indiqué au niveau de chaque ligne de commande du terminal entre parenthèses



from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

while True:
    clock.tick(1)

    for event in pg.event.get():
        pass

    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    screen.fill(random_color)
    pg.display.update()



# On ne peut fermer la fenetre avec la croix parce que : 