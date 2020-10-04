import pygame
from pygame.sprite import Sprite 

class Virus(Sprite):
    """Represent a single virus in the fleet."""
    
    def __init__(self, ai_game):
        """Initialize the virus and set it's starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the virus image and set its rect attribute.
        self.image = pygame.image.load('images/virus.png')
        self.rect  = self.image.get_rect()

        # Start each new virus near the top left of the screen.
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height 

        # Store the viruse's exact horizontal position.
        self.x = float(self.rect.x)