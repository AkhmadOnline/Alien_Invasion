import pygame

class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализирует настройки игры"""
        info = pygame.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.bg_color = (230, 230 , 230)
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        self.alien_speed = 1.0
        self.fleet_drop_speed = 5
        self.fleet_direction = 1