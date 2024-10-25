class Figure:
    sides_count = 0

    def __init__(self, rgb, *sides, filled=True):
        if not Figure.__is_valid_color(*rgb):
            raise TypeError

        self.__color = rgb

        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = sides

        if not self.__is_valid_sides(*self.__sides):
            raise TypeError

        self.filled = filled

    def __len__(self):
        return sum(self.__sides)

    def __repr__(self):
        attrs = ', '.join([f'{key}={getattr(self, key)}' for key in sorted(self.__dict__)])
        return f'{self.__class__.__name__} => {attrs}'

    def __is_valid_color(*rgb):
        if len(rgb) != 3:
            return False

        for color in rgb:
            if not isinstance(color, int) or color < 0 or color > 255:
                return False

        return True

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False

        for side in sides:
            if not isinstance(side, int) or side < 1:
                return False

        return True

    def get_color(self):
        return list(self.__color)

    def set_color(self, r, g, b):
        if Figure.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def get_sides(self):
        return list(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, rgb, *sides, filled=True):
        Figure.__init__(self, rgb, *sides, filled=filled)
        self.__radius = self.get_radius()

    def get_radius(self):
        return self.get_sides()[0] / (2 * 3.14)

    def get_square(self):
        return self.__radius ** 2 * 3.14

    def set_sides(self, *new_sides):
        Figure.set_sides(self, *new_sides)
        self.__radius = self.get_radius()


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = len(self) / 2
        sides = self.get_sides()
        return (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, rgb, *sides, filled=True):
        if len(sides) == 1:
            sides = sides * 12

        Figure.__init__(self, rgb, *sides, filled=filled)

    def get_volume(self):
        return self.get_sides()[0] ** 3

    def set_sides(self, *new_sides):
        if sum(new_sides) == new_sides[0] * len(new_sides):
            Figure.set_sides(self, *new_sides)


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((144, 144, 0), 10, 20, 30)

print(circle1)
print(cube1)
print(triangle1)
print()

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

print()
print(circle1)
print(cube1)
print(triangle1)
