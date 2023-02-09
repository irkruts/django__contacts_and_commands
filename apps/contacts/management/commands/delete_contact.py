import logging


from django.core.management import BaseCommand

from apps.contacts import models


class Command(BaseCommand):
    help = "Delete contact"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def handle(self, *args, **options):

        current_amount = models.Contacts.objects.all().count()
        self.logger.info(f"Current amount of contacts: {current_amount}")

        query = models.Contacts.objects.filter()  # is_auto_generated=True)
        total_amount, details = query.delete()

        self.logger.info(f"Amount of deleted animals : {total_amount}")

        amount_after_generation = models.Contacts.objects.all().count()
        self.logger.info(f"Amount of contacts after action: {amount_after_generation}")
