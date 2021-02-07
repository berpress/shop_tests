import faker


class UserData:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def random():
        fake = faker.Faker()
        return UserData(login=fake.email(), password=fake.password())


class UserDataNotRandom:
    def __init__(self, element, login, password):
        self.element = element
        self.login = login
        self.password = password

    def inp_value(self, login, password):
        if login is not None:
            self.element.send_keys(login)
        if password is not None:
            self.element.send_keys(password)
