# Створити клас Vehicle (транспортний засіб):
# ні від чого не наслідується
# в ініціалізатор класу (__init__ метод) передати
# producer: str
# model: str
# year: int
# tank_capacity: float # обєм паливного баку
# tank_level: float = 0 # початковий параметр рівня паливного баку дорівнює 0, параметр в аргументах не передавати
# maxspeed: int
# fuel_consumption: float # litres/100km споживання пального
# odometer_value: int = 0 # при сході з конвеєра пробіг нульовий, параметр в аргументах не передавати
#
# - визначити метод __repr__, яким повертати інформаційну стрічку (наповнення на ваш вибір, проте параметри model and
# year and odometer_value мають бути передані
#
# - написати метод refueling, який не приймає жодного аргумента, заправляє автомобіль на уявній автозаправці до
# максимума (tank_level = tank_capacity), після чого виводить на екран повідомлення, скільки літрів було заправлено
# (перша заправка буде повного баку, а в інших випадках величина буде залежати від залишку пального в баку)
#
# - написати метод race, який приймає один аргумент (не враховуючи self) - відстань, яку потрібно проїхати, а повертає
# словник, в якому вказано, скільки авто проїхало, з огляду на заповнення паливного баку перед поїздкою, залишок
# пального (при малому кілометражі все пальне не використається), та час, за який відбулася дана поїздка, з урахування,
# що середня швидкість складає 80% від максимальної (витрата пального рівномірна незалежно від швидкості)
#
# - за результатами роботи метода в атрибуті tank_level екземпляра класа має зберігатися залишок пального після поїздки
# (зрозуміло, що не менше 0)
#
# -  збільшити на величину поїздки показники odometer_value
#
# - написати метод lend_fuel, який приймає окрім self ще й other обєкт, в результаті роботи якого паливний бак обєкта,
# на якому було викликано відповідний метод, наповнюється до максимального рівня за рахунок відповідного зменшення рівня
# пального у баку дружнього транспортного засобу
#
# - вивести на екран повідомлення з текстом типу "Дякую, бро, виручив. Ти залив мені *** літрів пального"
#
# - у випадку, якщо бак першого обєкта повний або у другого обєкта немає пального, вивести повідомлення
# "Нічого страшного, якось розберуся"
#
# - написати метод __eq__, який приймає окрім self ще й other обєкт (реалізація магічного методу для оператора
# порівняння == )
#
# -  даний метод має повернути True у випадку, якщо 2 обєкта, які порівнюються, однакові за показниками року випуску та
# пробігу (значення відповідних атрибутів однакові, моделі можуть бути різними)
#
# -  створіть не менше 2-х обєктів класу, порівняйте їх до інших операцій, заправте їх, покатайтесь на них на різну
# відстань, перевірте пробіг, позичте один в одного пальне, знову порівняйте


class Vehicle:

    def __init__(self, producer: str, model: str, year: int, tank_capacity: float, tank_level: float, max_speed: int,
                 fuel_consumption: float, odometer_value: int
                 ):
        self.producer = producer
        self.model = model
        self.year = year
        self.tank_capacity = tank_capacity
        self.tank_level = tank_level
        self.max_speed = max_speed
        self.fuel_consumption = fuel_consumption
        self.odometer_value = odometer_value

    def __repr__(self):
        return f'Car models {self.model} went on sale in {self.year} year, the odometer was {self.odometer_value}'

    def __eq__(self, other):
        return (self.year, self.odometer_value) == (other.year, other.odometer_value)

    def re_fueling(self):
        """
This function is used on a class object, checks the difference between tank_level and tank_capacity values, after which
the tank_level value is automatically made equal to the tank_capacity value and a message is returned about how much
the tank_level value has changed.
        :return: (str)
        """
        filled = self.tank_capacity - self.tank_level
        if self.tank_capacity != self.tank_level:
            self.tank_level = self.tank_capacity
            return f'It was filled with {filled} liters.'

    def race(self, way):
        """
This function is for creating and filling a dictionary, depending on the value of the wey argument, and after the
comparison and calculations prescribed in this method, the values of the object, such as tank_level and
odometer_value, are overwritten.
        :param way: (int, float, >=0)
        :return:(dict)
        """
        max_way = self.tank_level * 100 / self.fuel_consumption
        if way > max_way:
            way = max_way
        self.odometer_value += way
        self.tank_level -= way * self.fuel_consumption / 100
        time = way / self.max_speed * 0.8
        return {
            'time': time,
            'way': way,
            'fuel': self.tank_level
        }

    def lend_fuel(self, other):
        """
The function first checks the tank_level value of two objects of the class and, based on the received one, either
replenishes the value of the first subtracting from the value of the other, while displaying a message in which it is
indicated how much this value has been filled;
or simply displays a message if the exchange is not possible.
        :param other:(int)
        :return: (str)
        """
        helped_refuel = self.tank_capacity - self.tank_level
        if self.tank_capacity == self.tank_level or other.tank_level == 0:
            return 'It\'s alright, I\'ll figure it out'
        if helped_refuel > other.tank_level:
            helped_refuel = other.tank_level
        self.tank_level += helped_refuel
        other.tank_level -= helped_refuel
        return f'Thank you, you filled me with {helped_refuel} liters.'


if __name__ == '__main__':
    auto_1 = Vehicle('car', 'Audi A6', 2015, 60, 0, 220, 10, 0)
    auto_2 = Vehicle('car', 'BMW X6', 2015, 90, 0, 240, 15, 0)
    print(auto_1, '\n', auto_2)
    print(auto_1 == auto_2)
    print(auto_2.re_fueling())
    print(Vehicle.lend_fuel(auto_1, auto_2))
    print(auto_2.tank_level)
    print(auto_2.race(100))
    print(auto_2.race(500))
    print(auto_1 == auto_2)