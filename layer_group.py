import pygame
from color_class import Color
from layer import Layer


class LayerGroup:
    def __init__(self, n, sz, start_color_range=Color(128, 128, 128), win=None):
        self.n = n
        self.sz = sz
        self.layers = []
        self.win = win

        layer_n = 4
        for i in range(n):
            self.layers.append(Layer(sz, layer_n + 1, start_color_range))
            layer_n *= 2
            start_color_range //= 2

    def show(self):
        if not self.win:
            print('Error, no window to show LayerGroup')
            return False

        for i in range(self.sz):
            for j in range(self.sz):
                color = Color(0, 0, 0)

                for layer in self.layers:
                    color += layer.pixels(i, j)

                pygame.draw.rect(self.win, color.tuple(), [i, j, 1, 1])

        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((1000, 1000))

    layer_group = LayerGroup(4, 512, win=win)
    layer_group.show()
    input()
