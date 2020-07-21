import os
from PIL import Image, ImageDraw
from color_class import Color
from layer_group import LayerGroup


class Map:
    def __init__(self, sz, range=100000, water_level=50000, snow_level=100000, make_clouds=True, water_around=True):
        self.sz = sz
        self.range = range
        self.water_level = water_level
        self.snow_level = snow_level
        self.make_clouds = make_clouds

        self.landscape = LayerGroup(22, sz, range, border_lower=water_level if water_around else None)
        if self.make_clouds:
            self.clouds = LayerGroup(22, sz, range)

        self.im = Image.new('RGBA', (self.sz, self.sz), 'black')
        self.pixels = self.im.load()
        self.height = []
        self.count_pixels()

    def show(self):
        self.im.show()

    def count_pixels(self):
        for i in range(self.sz):
            print(i / self.sz * 100, '%')
            self.height.append([])
            for j in range(self.sz):
                h = self.landscape[i, j]
                self.height[-1].append(h)
                global color
                if h < self.water_level:  # Water
                    color = Color(0, 0, h / 2 * 1000 / self.range)
                elif h < self.snow_level:
                    color = Color(h * 100 / self.range, h / 4 * 1000 / self.range, h / 30 * 1000 / self.range)
                else:
                    c = 1000
                    color = Color(c, c, c)

                if self.make_clouds:
                    color *= 0.2
                else:
                    color *= 0.4

                # Clouds
                if self.make_clouds:
                    h = (self.clouds[i, j] / self.range) ** 3 * self.range
                    color = (color + Color(h / 4 * 1000 / self.range, h / 4 * 1000 / self.range, h / 4 * 1000 / self.range) * 0.8)

                self.pixels[i, j] = int(color.r), int(color.g), int(color.b)

        arr = [int(filename.split('_')[0]) for filename in filter(lambda name: '_' in name, os.listdir('map_results'))]
        n = 1
        if arr:
            n += max(arr)
        self.im.save(f'map_results/{n}_map.png')

    def __getitem__(self, item):
        return self.height[item[0]][item[1]]


if __name__ == '__main__':
    map = Map(1024, make_clouds=False, water_around=True, water_level=10000)
    map.show()
    input()
