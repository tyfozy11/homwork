# Task 1.
# Доопрацюйте класс Line так, щоб в атрибути begin та end обʼєктів цього класу можна було записати тільки обʼєкти
# класу Point. Використовуйте property
# Task 2.
# Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point). Реалізуйте перевірку даних,
# аналогічно до класу Line. Визначет атрибут, що містить площу трикутника (за допомогою property). Для обчислень можна
# використати формулу Герона (https://en.wikipedia.org/wiki/Heron%27s_formula)


class Point:
    _x = None
    _y = None

    @property  # getter
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._x = value

    @property  # getter
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._y = value

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord


class Line:
    begin = None
    end = None

    def __init__(self, begin_point: Point, end_point: Point):
        self.begin = begin_point
        self.end = end_point

    @property
    def length(self):
        print('in length_getter')
        return ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5


class Triangle:
    point1 = None
    point2 = None
    point3 = None

    def __init__(self, point_1: Point, point_2: Point, point_3: Point):
        self.point1 = point_1
        self.point2 = point_2
        self.point3 = point_3

    def calculate_the_area_of_a_triangle(self):
        self.side_1 = Line(point1, point2)
        self.side_2 = Line(point2, point3)
        self.side_3 = Line(point1, point3)

        p = ((self.side_1 + self.side_2 + self.side_3) * 0.5)

        S = (p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3)) ** 0.5
        return S


if __name__ == '__main__':
    point_1 = Point(0, 3)
    point_2 = Point(4, 0)
    point_3 = Point(3, 4)