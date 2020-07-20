from layer_group import LayerGroup
import pygame


class Map:
    def __init__(self, sz, win):
        self.sz = sz
        self.win = win

        self.landscape = LayerGroup(22, sz, 1000)

    def show(self):
        for i in range(self.sz):
            print(i / self.sz, '%')
            for j in range(self.sz):
                if self.landscape[i, j] < 500:  # Water
                    pygame.draw.rect(self.win, (0, 0, self.landscape[i, j] / 2), [i, j, 1, 1])
                else:
                    pygame.draw.rect(self.win,
                                     (self.landscape[i, j] / 10, self.landscape[i, j] / 4, self.landscape[i, j] / 30),
                                     [i, j, 1, 1])

        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((1000, 1000))

    map = Map(512, win)
    map.show()
    input()
