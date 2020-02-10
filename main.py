##########################
# Author: PZmyslony
# Module Name: Rectangle
# Date: 10/02/2020
# Version: 0.1a
##########################
import pygame


class Rectangle:
    def __init__(self, width, height):
        self.image = pygame.Surface(size)
        self.image.fill(colortpl)
        
        # Draw the rectangle
        pygame.draw.rect(self.image, color, [0, 0, size[0], size[1]])
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        pass

    def area(self, area):
        pass

    def perimeter(self, perimeter):
        pass

    def setColor(self, colortpl):
        self.image.set_colorkey(colortpl)
        return self

    def draw(self):
        pass
