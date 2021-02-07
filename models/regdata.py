from faker import Faker
from random import randint


fake = Faker("ru_Ru")


class RegData:
    def __init__(self, passwd, firstname, lastname, years):
        self.passwd = passwd
        self.firstname = firstname
        self.lastname = lastname
        self.years = years

    @staticmethod
    def random():
        return RegData(
            password=fake.password(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            years=randint(1, 100),
        )
