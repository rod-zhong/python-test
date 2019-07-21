import game_functions as gf
import pygame
from setting import Setting
from ship import Ship

"""
    main functions to start run game
"""


def run_game():
    pygame.init()
    game_setting = Setting()
    screen = pygame.display.set_mode((game_setting.height, game_setting.width))  # screen resolution
    pygame.display.set_caption("Alien Invasion")  # screen title 
    mother_ship = Ship(screen)  # create mother ship 
    while True:
        gf.check_events(mother_ship)
        mother_ship.update()
        gf.update_screen(game_setting, screen, mother_ship)


run_game()
