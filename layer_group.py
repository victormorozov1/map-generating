import pygame
from color_class import Color
from layer import Layer, ColorLayer


class LayerGroup:
    def __init__(self, n, sz, start_range, win=None, layer_class=Layer, start_n=4):
        self.n = n
        self.sz = sz
        self.layers = []
        self.win = win
        self.start_range = start_range
        self.layer_class = layer_class

        layer_n = start_n
        for i in range(n):
            start_range = (start_range - 1) // 2 + 1
            if start_range < 2:
                self.n = i + 1
                print(f'self.n = {self.n}')
                break

            new_layer = self.layer_class(self.sz, layer_n + 1, start_range)
            if new_layer.cell_sz == 0:
                self.n = i + 1
                print(f'self.n = {self.n}')
                break

            self.layers.append(new_layer)
            layer_n *= 2

    def count_color(self, i, j):
        c = self[i, j] / self.start_range * 255
        return Color(c, c, c)

    def show(self):
        if not self.win:
            print('Error, no window to show LayerGroup')
            return False

        for i in range(self.sz):
            print(f'{i / self.sz * 100}%')
            for j in range(self.sz):
                global color
                color = self.count_color(i, j)
                if isinstance(color, Color):
                    color = color.tuple()
                pygame.draw.rect(self.win, color, [i, j, 1, 1])

        pygame.display.update()

    def __getitem__(self, item):
        return sum([layer[item] for layer in self.layers])


class ColorLayerGroup(LayerGroup):
    def __init__(self, *args, win=None, layer_class=ColorLayer):
        super().__init__(*args, win=win, layer_class=ColorLayer)

    def count_color(self, i, j):
        color = Color(0, 0, 0)

        for layer in self.layers:
            color += layer.pixels(i, j)

        return color


if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((1024, 1024))

    layer_group = ColorLayerGroup(33, 512, Color(1, 256, 256), win=win)
    layer_group.show()
    input()
