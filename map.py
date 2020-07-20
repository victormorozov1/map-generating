import os
from PIL import Image, ImageDraw
from color_class import Color
from layer_group import LayerGroup


class Map:
    def __init__(self, sz, range=100000, water_level=50000, snow_level=80000):
        self.sz = sz
        self.range = range
        self.water_level = water_level
        self.snow_level = snow_level

        self.landscape = LayerGroup(22, sz, range)
        self.clouds = LayerGroup(22, sz, range)

    def show(self):
        im = Image.new('RGBA', (self.sz, self.sz), 'black')
        pixels = im.load()

        for i in range(self.sz):
            print(i / self.sz * 100, '%')
            for j in range(self.sz):
                h = self.landscape[i, j]
                global color
                if h < self.water_level:  # Water
                    color = Color(0, 0, h / 2 * 1000 / self.range)
                elif h < self.snow_level:
                    color = Color(h * 100 / self.range, h / 4 * 1000 / self.range, h / 30 * 1000 / self.range)
                else:
                    c = h / 8 * 1000 / self.range + 128
                    color = Color(c, c, c)
                color *= 0.2

                # Clouds
                h = (self.clouds[i, j] / self.range) ** 3 * self.range
                color = (color + Color(h / 4 * 1000 / self.range, h / 4 * 1000 / self.range, h / 4 * 1000 / self.range) * 0.8).tuple()
                pixels[i, j] = int(color[0]), int(color[1]), int(color[2])

        im.show()

        arr = [int(filename.split('_')[0]) for filename in filter(lambda name: '_' in name, os.listdir('map_results'))]
        n = 1
        if arr:
            n += max(arr)
        im.save(f'map_results/{n}_map.png')


if __name__ == '__main__':
    map = Map(2048)
    map.show()
    input()
