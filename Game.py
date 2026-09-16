
##Flower Bouqet App

"""
The goal of this app is to let the user chose a pot color, a flower of their choice,
water it until it grows, once it is grown they can save it to their inventory until they have 12 flowers to make a bouqet to gift to their mother.
"""

##import pygame
"""
pygame is used for turning the python game class from running through a console, to running through an interactive game window
"""
import pygame

class Game:

    """
    Making Buttons
    """
    
    # Top center
    top_center = pygame.Rect(300, 20, 200, 75)
    # Top right
    top_right = pygame.Rect(680, 20, 100, 75)
    # Bottom left
    bottom_left = pygame.Rect(20, 505, 150, 75)
    # Bottom right
    bottom_right = pygame.Rect(630, 505, 150, 75)
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Bouquet Builder")

    running = True

    while running:

        ##show buttons
        pygame.draw.rect(screen, "white", top_center)
        pygame.draw.rect(screen, "white", top_right)
        pygame.draw.rect(screen, "white", bottom_left)
        pygame.draw.rect(screen, "white", bottom_right)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()