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
        if self.year and self.odometer_value == other.year and other.odometer_value:
            return True

    def re_fueling(self):
        self.filled = self.tank_capacity - self.tank_level
        if self.tank_capacity != self.tank_level:
            return f'It was filled with {self.filled} liters.'

    def race(self, other):
        self.average_speed = self.max_speed * 0, 8
        self.time_race = self
        return

    def lend_fuel(self, oder):
        self.helped_refuel = self.tank_capacity - self.tank_level
        if self.tank_capacity < oder.tank_level:
            self.tank_capacity = oder.tank_level - self.helped_refuel
            return f'Thank you, you filled me with {self.helped_refuel} liters.'
        if self.tank_capacity == self.tank_level or oder.tank_level == 0:
            return 'It\'s alright, I\'ll figure it out'


if __name__ == '__main__':
    auto_1 = Vehicle('car', 'Audi A6', 2015, 60, 40, 220, 10, 0)
    auto_2 = Vehicle('car', 'BMW X6', 2015, 90, 80, 240, 15, 0)
    print(auto_1, '\n', auto_2)
    # print(auto_1.re_fueling())
    print(auto_2.re_fueling())
    print(Vehicle.lend_fuel(auto_1, auto_2))
    print(auto_2.tank_level)
