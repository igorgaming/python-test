class Parallelepiped:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height

    def get_volume(self):
        return self.width * self.height * self.length

    def get_base_square(self):
        return self.width * self.height

    def get_side_square(self):
        return 2 * (self.width * self.height + self.length * self.height)

    @staticmethod
    def info():
        return print(dir(Parallelepiped))

figure = Parallelepiped(10, 15, 20)
print(f"Volume = {figure.get_volume()}, Base square = {figure.get_base_square()}, Side square = {figure.get_side_square()}")
Parallelepiped.info()
