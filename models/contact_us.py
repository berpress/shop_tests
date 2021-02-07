class ContactUsData:
    def __init__(self, element, value, address, order, message):
        self.element = element
        self.value = value
        self.address = address
        self.order = order
        self.message = message

    def input_value(self, element, value, address, order, message):
        if value is not None:
            self.element.select_by_value(value)
        if address is not None:
            self.element.send_keys(address)
        if order is not None:
            self.element.send_keys(order)
        if message is not None:
            self.element.send_keys(message)
