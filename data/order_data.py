import random
from faker import Faker

faker = Faker("ru_RU")


class UserMale:
    phone = random.randint(11111111111, 99999999999)
    name_1 = faker.first_name_male()
    last_name_1 = faker.last_name_male()
    address_1 = 'Москва, Новоясевская'
    metro_station_1 = 'Новоясевская'
    date_1 = '20.01.2024'
    rental_period_1 = 0
    scooter_finish_1 = 0
    comment_1 = 'Спасибо'


class UserFemale:
    phone = random.randint(11111111111, 99999999999)
    name_2 = faker.first_name_female()
    last_name_2 = faker.last_name_female()
    address_2 = 'Москва, Мякинино'
    metro_station_2 = 'Мякинино'
    date_2 = '10.12.2022'
    rental_period_2 = 6
    scooter_finish_2 = 1
    comment_2 = 'Жду самокат:)'
