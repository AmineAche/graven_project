from dataclasses import dataclass

import pygame
import pyscroll
from pytmx import util_pygame


@dataclass
class Map:
    name: str
    walls: list[pygame.Rect]
    group: pyscroll.PyscrollGroup


class MapManager:

    def __init__(self, screen, player):
        self.maps = dict()  # "house" -> Map("house", walls, group)
        self.screen = screen
        self.player = player
        self.current_map = "carte"

        self.register_map("carte")
        self.register_map("house")

    def register_map(self, name):
        # Charger la carte tmx
        tmx_data = util_pygame.load_pygame('../map/carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Les collisions
        walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        group.add(self.player)

        # Cree objet Map
        self.maps[name] = Map(name, walls, group)

    def get_map(self):
        return self.maps[self.current_map]

    def get_group(self):
        return self.get_map().group

    def get_walls(self):
        return self.get_map().walls

    def draw(self):
        self.get_group().draw(self.screen)

        self.get_group().center(self.player.rect.center)

    def update(self):
        self.get_group().update()
