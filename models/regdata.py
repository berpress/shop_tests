from faker import Faker
from random import randint


fake = Faker("ru_Ru")


class RegData:
    def __init__(self, passwd, firstname, lastname, years, login):
        self.passwd = passwd
        self.firstname = firstname
        self.lastname = lastname
        self.years = years
        self.login = login

    @staticmethod
    def random():
        return RegData(
            passwd=fake.password(),
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            years=randint(1, 100),
            login=fake.email()
        )
