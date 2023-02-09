from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    __repr__ = __str__


class Contacts(models.Model):
    name = models.CharField(max_length=20, verbose_name="Name")
    phone = models.CharField(max_length=20, verbose_name="Phone number", blank=True)
    date_of_birth = models.DateField(
        null=True, verbose_name="Date of birth", blank=True
    )
    is_auto_generated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated date")

    group = models.ForeignKey(
        Group,
        related_name="contacts_group",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
    )

    objects = models.Manager()


class Meta:
    verbose_name = "Contact"
    verbose_name_plural = "Contacts"
