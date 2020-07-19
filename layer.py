from color_class import Color
import pygame
from random import randrange as rd


class Layer:
    def __init__(self, sz, n, color_range, win=None):
        self.sz = sz
        self.n = n
        self.color_range = color_range
        self.win = win

        self.cell_sz = self.sz // (n - 1)

        self.arr = []
        self.create_arr()
        print(f'cell_sz = {self.cell_sz}')

    def create_arr(self):
        for i in range(self.n):
            self.arr.append([])
            for j in range(self.n):
                self.arr[-1].append(Color(color_range=self.color_range))

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

    layer = Layer(512, 17, (100, 100, 100), win)
    layer.show()
    input()





