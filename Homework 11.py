# Task 1.
# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від "Транспортний засіб".
# Наповніть класи атрибутами на свій розсуд. Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель"


class Vehicle:
    passenger_capacity = None
    travel_environment = None
    movement_speed = None

    def __init__(self, new_passenger_capacity, new_travel_environment, new_movement_speed):
        self.passenger_capacity = new_passenger_capacity
        self.travel_environment = new_travel_environment
        self.movement_speed = new_movement_speed

    def description(self):
        return f'Short description:\n\ntravel_environment-{self.travel_environment};' \
               f'\npassenger capacity-{self.passenger_capacity};\n' \
               f'movement speed-{self.movement_speed}.'


class Automobile(Vehicle):
    complexity_of_management = 'easily'


car = Automobile('Small(1-5)', 'ground', 'average')

print(car.description())


class Airplane(Vehicle):
    range_of_flight = 'medium-haul'


passenger_plane = Airplane('average (100-250)', 'air space', 'high')


class Ship(Vehicle):
    vessel_class = 'Oasys'


cruise_ship = Ship('very large (up to 5500)', 'expanses of water', 'slowly')

print(cruise_ship.passenger_capacity)
