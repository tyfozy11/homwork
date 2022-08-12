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


point1 = Point(0, 3)
# point1.x = 100
point2 = Point(4, 0)
point3 = Point(4, 3)


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


line1 = Line(point2, point1)
line2 = Line(point1, point3)
line3 = Line(point2, point3)

print(line1.length)
print(line2.length)
print(line3.length)


class Triangle:
    side_a = line1
    side_b = line2
    side_c = line3

    def __init__(self, side_a_line, side_b_line, side_c_line):
        self.side_a = side_a_line
        self.side_b = side_b_line
        self.side_c = side_c_line

    def calculate_the_area_of_a_triangle(self):
        p = ((self.side_a + self.side_b + self.side_c) * 0.5)
        S = (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5
        return S
