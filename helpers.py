import random
from faker import Faker

stations = [
    "Черкизовская",
    "Комсомольская",
    "Арбатская",
    "Тверская"
]

faker = Faker('ru_RU')
def generate_personal_information():
    name = faker.first_name()
    lastname = faker.last_name()
    address = AddressGenerator.generate_moscow_address_with_random_street()
    station = random.choice(stations)
    phone = '+79' + ''.join(random.choices('0123456789', k=9))

    return name, lastname, address, station, phone

class AddressGenerator:
    streets = [
        "Тверская улица",
        "Арбат",
        "Ленинградский проспект",
        "Проспект Мира",
        "Новая Басманная улица",
        "Садовая-Кудринская улица",
        "Пятницкая улица",
        "Большая Никитская улица",
        "Кузнецкий Мост",
        "Профсоюзная улица",
        "Улица 1905 года",
        "Рублёвское шоссе",
        "Каширское шоссе",
        "Ярославское шоссе"
    ]

    @staticmethod
    def generate_moscow_address_with_random_street():
        street = random.choice(AddressGenerator.streets)
        return f"Москва, {street}"
