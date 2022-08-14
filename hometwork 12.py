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

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._x = value

    @property
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
    _begin = None
    _end = None

    @property
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._begin = value

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._end = value

    def __init__(self, begin_point, end_point):
        self.begin = begin_point
        self.end = end_point

    @property
    def length(self):
        """
        The function, based on objects of the class Point, creates two points (beginning and end), after which it
        calculates the length of the retract between them and returns the result of the calculation.

        :return: (float)
        """
        return ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5


class Triangle:
    _point1 = None
    _point2 = None
    _point3 = None

    @property
    def point1(self):
        return self._point1

    @point1.setter
    def point1(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._point1 = value

    @property
    def point2(self):
        return self._point1

    @point2.setter
    def point2(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._point2 = value

    @property
    def point3(self):
        return self._point3

    @point3.setter
    def point3(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._point3 = value

    def __init__(self, point_1: Point, point_2: Point, point_3: Point):
        self.point1 = point_1
        self.point2 = point_2
        self.point3 = point_3

    @property
    def calculate_the_area_of_a_triangle(self):
        """
        This function is for calculating the area of a triangle and using Heron's formula. First, from the
         received objects of the Point class, using the length method of the Line class, it creates and calculates the
          length of the sides, after which the obtained data is substituted into the formula and at the end the result
          of the calculation is returned, which is the area of the triangle obtained from the points.


        :return: (float)
        """
        self.side_1 = Line(self._point1, self._point2).length
        self.side_2 = Line(self._point2, self._point3).length
        self.side_3 = Line(self._point1, self._point3).length

        p = ((self.side_1 + self.side_2 + self.side_3) * 0.5)

        S = (p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3)) ** 0.5
        return S


if __name__ == '__main__':
    point1 = Point(0, 0)
    point2 = Point(3, 0)
    point3 = Point(0, 4)
    tr = Triangle(point1, point2, point3)
    print(tr.calculate_the_area_of_a_triangle)
