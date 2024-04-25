

class Ex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z


class Ex2(Ex):
    pass


class Extended(Ex):
    def __init__(self, x, y, z, color=None):
        super(Extended, self).__init__(x, y, z)
        if not color:
            self.color = "Gray"

    def volume_and_color(self):
        return self.x * self.y * self.z, self.color


if __name__ == '__main__':
    a = Extended(4, 10, 3)
    print(a.volume())
    print(a.volume_and_color())
    b = Ex2(1, 2, 3)
    print(b.volume())
