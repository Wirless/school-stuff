##########################
# Author: PZmyslony
# Module Name: Rectangle
# Date: 10/02/2020
# Version: 0.1a
##########################
import pygame


pygame.init()
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rectangling")

class Rectangle(pygame.sprite.Sprite):
    def __init__(self, size, color, pos):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill((255,0,0))
        self.image.set_colorkey((255,0,0))
        pygame.draw.rect(self.image, color, [0, 0, size[0], size[1]])
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        
    def area(self):
        area = self.rect
        newarea = area[2]+area[3]
        return area

    def perimeter(self, perimeter):
        pass

    def setColor(self, colortpl):
        self.image.set_colorkey(colortpl)
        return self

    def draw(self):
        pass


## size = (width , height)  / (colortpl) , pos =(positionx,positiony)
box = Rectangle((80, 200), (200,0,0),(250, 250))

box2 = Rectangle((20, 100), (100,10,50),(450, 150))

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(box,box2)

clock = pygame.time.Clock()

print(box2.area)

carryOn = True
print(box.__init__)
while carryOn:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            all_sprites_list.update()
            screen.fill((255,255,255))
            all_sprites_list.draw(screen)
            pygame.display.flip()
            clock.tick(60)
pygame.quit()
