import pygame

class Doctor:
    """Manage the doctor"""

    def __init__(self, ai_game):
        """Initialize the doctor and set his starting position."""
        self.screen      = ai_game.screen
        self.settings    = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the doctor image and get it's rect.
        self.image = pygame.image.load('images/nurse.png')
        self.rect  = self.image.get_rect()

        # Start each new doctor at the bottom middle of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the doctor's horizontal position.
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update doctor's position based on movement flags"""
        # Update doctor's x value not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.doctor_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.doctor_speed
        
        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the doctor at his current location."""
        self.screen.blit(self.image, self.rect)

