import pygame
import pyscroll
from pytmx import *

from src.map import MapManager
from src.player import Player


class Game:

    def __init__(self):

        # Affichage de la fenêtre
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Basique - Game")



        # Générer le joeur
        self.player = Player(0, 0)
        self.map_manager = MapManager(self.screen, self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_player("up")
        elif pressed[pygame.K_DOWN]:
            self.player.move_player("down")
        elif pressed[pygame.K_RIGHT]:
            self.player.move_player("right")
        elif pressed[pygame.K_LEFT]:
            self.player.move_player("left")

    def update(self):
        self.map_manager.update()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        # Clock
        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()
