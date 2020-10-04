class Settings:
    """Stores all the game settings."""

    def __init__(self):
        """Initialize game settings."""

        # Screen settings.
        self.screen_width  = 1200
        self.screen_height = 800
        self.bg_color      = (230, 230, 230)
        self.doctor_speed  = 1.5

        # vaccine settings.
        self.vaccine_speed   = 1.0
        self.vaccine_allowed = 3