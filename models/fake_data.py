from faker import Faker

fake = Faker("ru_Ru")


class UserData:
    def __init__(self, login, password, first_name, last_name):
        self.login = login
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def random():
        return UserData(
            login=fake.email(),
            password=fake.password(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
        )


class Address:
    def __init__(
        self,
        company,
        email,
        address,
        city,
        country,
        phone,
        building,
        street,
    ):
        self.company = company
        self.email = email
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
            email=fake.email(),
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


class PersonalInformationData:
    def __init__(self, login, password, firstname, lastname, years):
        self.login = login
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.years = years

    @staticmethod
    def random():
        return PersonalInformationData(
            login=fake.email(),
            password=fake.password(),
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            years=fake.year(),
        )
