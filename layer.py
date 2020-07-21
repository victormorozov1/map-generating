from color_class import Color
import pygame
from random import randrange as rd


class Layer:
    def __init__(self, sz, n, range, win=None, border=None):
        self.sz = sz
        self.n = n
        self.range = range
        self.win = win
        self.border = border

        self.cell_sz = self.sz // (n - 1)

        self.arr = []
        self.create_arr()
        print(f'cell_sz = {self.cell_sz}')
        print(f'self.border={self.border}')

    def new_random_item(self, range=None):
        return rd(0, range if range else self.range)

    def create_arr(self):
        for i in range(self.n):
            self.arr.append([])
            for j in range(self.n):
                if self.border and i * j * (i - self.n + 1) * (j - self.n + 1) == 0:
                    self.arr[-1].append(self.new_random_item(range=self.border))
                else:
                    self.arr[-1].append(self.new_random_item())

    def parabola(self, x):
        return x ** 2 * (0.5 / 0.25)

    def double_parabola(self, x):
        if x < 0.5:
            return self.parabola(x)
        return 1 - self.parabola(1 - x)

    def f(self, v1, v2, k):
        k = self.double_parabola(k)
        return v1 * (1 - k) + v2 * k

    def pixels(self, i, j):
        arr_i = i // self.cell_sz
        arr_j = j // self.cell_sz

        val_up = self.f(self.arr[arr_i][arr_j], self.arr[arr_i][arr_j + 1], j % self.cell_sz / self.cell_sz)
        val_down = self.f(self.arr[arr_i + 1][arr_j], self.arr[arr_i + 1][arr_j + 1], j % self.cell_sz / self.cell_sz)

        return self.f(val_up, val_down, i % self.cell_sz / self.cell_sz)

    def color(self, i, j):
        color = self.pixels(i, j) / self.range * 255
        return Color(color, color, color)

    def show(self):
        if not self.win:
            print('Error, no window to show layer')
            return False

        for i in range(self.sz):
            for j in range(self.sz):
                pygame.draw.rect(self.win, self.color(i, j), [i, j, 1, 1])

        pygame.display.update()

    def __getitem__(self, item):
        return self.pixels(*item)

    def __setitem__(self, key, value):
        self.arr[key[0]][key[1]] = value


class ColorLayer(Layer):
    def new_random_item(self):
        return Color(color_range=self.range)

    def color(self, i, j):
        return self.pixels(i, j)

    def show(self):
        if not self.win:
            print('Error, no window to show layer')
            return False

        for i in range(self.sz):
            for j in range(self.sz):
                pygame.draw.rect(self.win, self.pixels(i, j).tuple(), [i, j, 1, 1])

        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((1000, 1000))

    layer = ColorLayer(8, 17, (255, 255, 255), win)
    print(layer[3, 4])
    input()





