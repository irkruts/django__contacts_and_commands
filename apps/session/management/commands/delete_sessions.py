import logging


from django.core.management import BaseCommand, CommandParser

from apps.contacts import models


class Command(BaseCommand):
    help = "Delete session info"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def add_arguments(self, parser: CommandParser):
        parser.add_argument("--delete_sessions", help="Delete session info")

    def handle(self, *args, **options):

        current_sessions_amount = models.UserDataRequest.objects.all().count()
        self.logger.info(f"Current amount of sessions: {current_sessions_amount}")

        query = models.UserDataRequest.objects.all()
        current_sessions_amount, details = query.delete()

        self.logger.info(f"Amount of deleted sessions : {current_sessions_amount}")

        amount_after_deleted = models.Contacts.objects.all().count()
        self.logger.info(f"Amount of sessions after action: {amount_after_deleted}")
