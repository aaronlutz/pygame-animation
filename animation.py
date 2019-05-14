import os
import pygame
from win32api import GetSystemMetrics
from character2 import Character
import game_functions as gf
from slider import Slider
from settings import Settings
from scene import Scene


def run_game():
    # Initialize pygame, settings, and screen object
    settings = Settings()
    pygame.init()
    pygame.display.set_caption("Maze Runner")
    screen = pygame.display.set_mode(settings.screen_dim)
    little_dude = Character(settings)
    #slider = Slider(settings)
    scene = Scene(screen, settings)

    readouts = gf.create_read_outs(screen, settings, little_dude)

    while True:

        gf.check_events(little_dude)
        gf.update_screen(screen, settings, little_dude, scene, readouts)
        #if not slider.clicked:
        pygame.time.wait(60)


run_game()
