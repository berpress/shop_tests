import faker


class ContactUsData:
    def __init__(self, value, address, order, message):
        self.value = value
        self.address = address
        self.order = order
        self.message = message

    @staticmethod
    def random():
        fake = faker.Faker()
        return ContactUsData(
            value="1",
            address=fake.email(),
            order=fake.postcode(),
            message="Random Message",
        )
