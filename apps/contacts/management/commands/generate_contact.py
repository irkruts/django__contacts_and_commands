import logging


from django.core.management import BaseCommand, CommandParser
from apps.contacts.services import generate_contact

from apps.contacts import models


class Command(BaseCommand):
    help = "Generate required amount of contacts"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "--amount", type=int, default=10, help="Amount of generated contacts"
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]
        self.logger.info(f"Generate {amount} contacts")

        current_amount = models.Contacts.objects.all().count()
        self.logger.info(f"Current amount of contacts: {current_amount}")

        for count, contact in enumerate(generate_contact(amount=amount), start=1):
            self.logger.info(f"Generate: {amount} of {amount}.Start")
            contact.is_auto_generated = True
            contact.save()
            self.logger.info(f"Generate: {amount} of {amount}. End")

        amount_after_generation = models.Contacts.objects.all().count()
        self.logger.info(
            f"Amount of contacts after generation: {amount_after_generation}"
        )
