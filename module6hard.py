import math


class Figure:  # класс фигуры
    sides_count = 0  # количество сторон

    def __init__(self, __color: tuple, *__sides: int, filled: bool = True):
        if len(__sides) != self.sides_count:
            self.__sides = [1 * self.sides_count]
        else:
            self.__sides = [i for i in __sides]
        self.__color = __color
        self.__filled = filled

    def get_color(self):#возвращает список RGB цветов
        return [i for i in self.__color]

    def __is_valid_color(self, r, g, b):# служебный метод проверки цвета
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
                return False
        return True

    def set_color(self, r, g, b):# установка цвета фигуры
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self,*sides):## служебный метод проверки количества сторон
        result = [i for i in sides if i > 0]
        if len(result) == self.sides_count:
            return True
        return False

    def get_sides(self):  # возвращает список сторон
        return [*self.__sides]

    def __len__(self):  # возвращает периметр фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides):  # установка количества сторон
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides
        return self.__sides # возвращает список сторон


class Circle(Figure):## класс круга
    sides_count = 1## количество сторон

    def __radius(self):# возвращает радиус круга
        radius = self.__len__ / (2 * math.pi)
        return radius

    def  get_square(self):## возвращает площадь круга
        S = self.__radius()**2*math.pi
        return S


class Triangle(Figure):## класс треугольника
    sides_count = 3## количество сторон

    def get_square(self):## возвращает площадь треугольника
        semiperimeter =self.__len__ / 2
        S = math.sqrt((semiperimeter (semiperimeter - self.__sides[0]) (semiperimeter-self.__sides[1])
                       (semiperimeter-self.__sides[2])))
        return S

class Cube(Figure):# класс куба
    sides_count = 12# количество сторон

    def __init__(self, __color: tuple, *__sides: int, filled: bool = True):
        super().__init__(__color, *__sides, filled)  # вызов конструктора
        if len(__sides) == 1:
            self.__sides =  self.sides_count*[i for i in __sides]
        else:
            self.__sides = [1*self.sides_count]



    def get_sides(self):
        return [*self.__sides] # возвращает список сторон

    def get_volume(self):
        return self.__sides[1]**3

if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)
    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())
    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())
    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())









