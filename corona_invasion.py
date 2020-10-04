import sys
import pygame

from settings import Settings
from doctor import Doctor
from vaccine import Vaccine
from virus import Virus

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
        self.virus   = pygame.sprite.Group()

        self._create_fleet()

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

    def _create_fleet(self):
        """Create a fleet of virus."""
        # Create a virus and find a number of virus in the row.
        # Spacing between each virus is equal to one virus width.
        virus = Virus(self)
        virus_width, virus_height = virus.rect.size
        available_space_x         = self.settings.screen_width - (2 * virus_width)
        number_virus_x            = available_space_x // (2 * virus_width)

        # Determine the number of virus rows that fir to the screen.
        doctor_height     = self.doctor.rect.height 
        available_space_y = (self.settings.screen_height - (3 * virus_height) - doctor_height)
        number_rows       = available_space_y // (2 * virus_height)

        # Create full fleet of virus.
        for row_number in range(number_rows):
            for virus_number in range(number_virus_x):
                self._create_virus(virus_number, row_number)

    def _create_virus(self, virus_number, row_number):
        """Create virus and place it in the row"""
        virus                      = Virus(self)
        virus_width, virus_height  = virus.rect.size
        virus.x                    = virus_width + 2 * virus_width * virus_number
        virus.rect.x               = virus.x 
        virus.rect.y               = virus.rect.height + 2 * virus.rect.height * row_number

        self.virus.add(virus)

    def _update_screen(self):
        """Update images on the screen and flip to new screen."""
        self.screen.fill(self.settings.bg_color)
        self.doctor.blitme()
        for vaccine in self.vaccine.sprites():
            vaccine.draw_vaccine()
        self.virus.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = CoronaInvasion()
    ai.run_game()

