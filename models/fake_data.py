from faker import Faker

fake = Faker("ru_Ru")


class RegData:
    def __init__(self, login, password, first_name, last_name):
        self.login = login
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def random():
        return RegData(
            login=fake.email(),
            password=fake.password(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
        )


class Address:
    def __init__(
        self,
        company,
        address,
        city,
        country,
        phone,
        building,
        street,
    ):
        self.company = company
        self.address = address
        self.city = city
        self.country = country
        self.phone = phone
        self.building = building
        self.street = street

    @staticmethod
    def random():
        return Address(
            company=fake.company(),
            address=fake.address(),
            city=fake.city(),
            country=fake.country(),
            phone=fake.phone_number(),
            building=fake.building_number(),
            street=fake.street_name(),
        )


class Date:
    def __init__(self, year, month, month_name, day):
        self.year = year
        self.month = month
        self.month_name = month_name
        self.day = day

    @staticmethod
    def random():
        return Date(
            year=fake.year(),
            month=fake.month(),
            month_name=fake.month_name(),
            day=fake.day_of_month(),
        )
