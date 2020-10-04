import pygame
from pygame.sprite import Sprite 

class Vaccine(Sprite):
    """Manage vaccines doctor fires to virus."""

    def __init__(self, ai_game):
        """Create a vaccine object at the doctor's current position"""
        super().__init__()
        self.screen   = ai_game.screen
        self.settings = ai_game.settings
        # self.color    = self.settings.vaccine_color
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/pill.png')
        self.rect  = self.image.get_rect()

        self.rect.midright = ai_game.doctor.rect.midright

        # Store the vaccine's position as a decimal value.
        self.y = float(self.rect.y)

    
    def update(self):
        """Move the vaccine up the screen."""
        # Update the decimal position of the vaccine.
        self.y -= self.settings.vaccine_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_vaccine(self):
        """Draw the vaccine to the screen."""
        self.screen.blit(self.image, self.rect)



