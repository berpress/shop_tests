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
        address,
        city,
        state,
        postal_code,
        country,
        mobile_phone,
        building,
        street,
    ):
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.mobile_phone = mobile_phone
        self.building = building
        self.street = street

    @staticmethod
    def random():
        return Address(
            company=fake.company(),
            address=fake.address(),
            city=fake.city(),
            state=fake.state(),
            postal_code=fake.postcode(),
            country=fake.country(),
            mobile_phone=fake.phone(),
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
