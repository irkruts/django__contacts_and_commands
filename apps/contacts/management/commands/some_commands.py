import logging


from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Experimental"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def handle(self, *args, **options):
        self.logger.info("Experemental")
        # group = models.Group.objects.first()
        # контактс_груп - потому, что в модели релейтед нейм = этому
        # по умолчанию названиемодели_set
        # related_contacts = group.contacts_group.all()
