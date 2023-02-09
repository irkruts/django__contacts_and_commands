from random import randint
from typing import Iterator

from faker import Faker
from .models import Contacts

faker = Faker()


def generate_contact(amount: int = 10) -> Iterator[Contacts]:
    date_of_birth = f"{randint(1950, 2022)}-{randint(1,12)}-{randint(1,31)}"
    phone_number = f"+38093{randint(1000000, 9999999)}"
    for _ in range(amount):
        yield Contacts(
            name=faker.name(),
            phone=phone_number,
            date_of_birth=date_of_birth,
        )
