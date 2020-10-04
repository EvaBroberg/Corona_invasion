import sys
import pygame

from settings import Settings
from doctor import Doctor
from vaccine import Vaccine

class CoronaInvasion:
    """Manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width  = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Corona Invasion')

        self.doctor  = Doctor(self)
        self.vaccine = pygame.sprite.Group()

        # Set background colour.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """"Start the main loop for the game."""
        while True:
            self._check_events()
            self.doctor.update()
            self._update_vaccine()
            self._update_screen()

    def _check_events(self):
        #watch for the keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                 self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key press."""
        if event.key == pygame.K_RIGHT:
            self.doctor.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.doctor.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_vaccine()

    def _check_keyup_events(self, event):
        """Respond to key release."""
        if event.key == pygame.K_RIGHT:
            self.doctor.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.doctor.moving_left = False

    def _fire_vaccine(self):
        """Create a new vaccine and add it to the vaccine group."""
        if len(self.vaccine) < self.settings.vaccine_allowed:
            new_vaccine = Vaccine(self)
            self.vaccine.add(new_vaccine)

    def _update_vaccine(self):
        """Update position of vaccine and get rid of old vaccine."""
        # Update vaccine positions.
        self.vaccine.update()

        # Get rid of vaccine that dissapeared.
        for vaccine in self.vaccine.copy():
            if vaccine.rect.bottom <= 0:
                self.vaccine.remove(vaccine)
    

    def _update_screen(self):
        """Update images on the screen and flip to new screen."""
        self.screen.fill(self.settings.bg_color)
        self.doctor.blitme()
        for vaccine in self.vaccine.sprites():
            vaccine.draw_vaccine()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = CoronaInvasion()
    ai.run_game()
