from random import randrange as rd


class Color:
    def __init__(self, *args, color_range=(256, 256, 256)):
        if args:
            self.r, self.g, self.b = args
        else:
            if isinstance(color_range, Color):
                color_range = color_range.tuple()
            self.r, self.g, self.b = rd(0, color_range[0]), rd(0, color_range[1]), rd(0, color_range[2])

    def __str__(self):
        return f'Color({self.r}, {self.g}, {self.b})'

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __sub__(self, other):
        return Color(self.r - other.r, self.g - other.g, self.b - other.b)

    def __mul__(self, other):
        return Color(self.r * other, self.g * other, self.b * other)

    def __mod__(self, other):
        if isinstance(other, Color):
            return Color(self.r % other.r, self.g % other.g, self.b % other.b)
        elif isinstance(other, tuple):
            return Color(self.r % other[0], self.g % other[1], self.b % other[2])
        return Color(self.r % other, self.g % other, self.b % other)

    def __imod__(self, other):
        return self % other

    def __floordiv__(self, other):
        if isinstance(other, Color):
            return Color(self.r // other.r, self.g // other.g, self.b // other.b)
        elif isinstance(other, tuple):
            return Color(self.r // other[0], self.g // other[1], self.b // other[2])
        return Color(self.r // other, self.g // other, self.b // other)

    def __ifloordiv__(self, other):
        return self // other

    def __iadd__(self, other):
        return self + other

    def __isub__(self, other):
        return self - other

    def __imul__(self, other):
        return self * other

    def tuple(self):
        return self.r, self.g, self.b


if __name__ == '__main__':
    c1 = Color(20, 30, 57)
    c2 = Color(10, 20, 1)
    c1 //= c2.tuple()
    print(c1, c2)
