import re
from field import Field

class Phone(Field):
    def __init__(self, number):
        self.value = self.validate(number)

    def validate(self, number):
        if not re.match(r"^\+?(\d{10})$", number.strip()):
            raise ValueError("Phone number should contain only digits")

        return number