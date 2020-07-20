from color_class import Color
from layer_group import LayerGroup
import pygame


class Map:
    def __init__(self, sz, win, range=1000, water_level=500, snow_level=800):
        self.sz = sz
        self.win = win
        self.range = range
        self.water_level = water_level
        self.snow_level = snow_level

        self.landscape = LayerGroup(22, sz, range)
        self.clouds = LayerGroup(22, sz, range)

    def show(self):
        for i in range(self.sz):
            print(i / self.sz * 100, '%')
            for j in range(self.sz):
                h = self.landscape[i, j]
                global color
                if h < self.water_level:  # Water
                    color = Color(0, 0, h / 2)
                elif h < self.snow_level:
                    color = Color(h / 10, h / 4, h / 30)
                else:
                    color = Color(h / 8 + 128, h / 8 + 128, h / 4)
                color *= 0.2

                # Clouds
                h = (self.clouds[i, j] / 1000) ** 3 * 1000
                color = color + Color(h / 4, h / 4, h / 4) * 0.8

                pygame.draw.rect(self.win, color.tuple(), [i, j, 1, 1])

        """for i in range(self.sz):
            print(50 + i / self.sz * 50, '%')
            for j in range(self.sz):
                h = self.clouds[i, j]
                if h > 600:
                    pygame.draw.rect(self.win, (100 + h / 7, 100 + h / 7, 10 + h / 7), [i, j, 1, 1]"""
        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((1111, 1111))

    map = Map(1024, win)
    map.show()
    input()
