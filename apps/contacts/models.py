import uuid

from django.db import models
from django.urls import reverse


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    __repr__ = __str__


def get_icon_path(instance, filename: str) -> str:
    _, extension = filename.rsplit(".", maxsplit=1)
    return f"contacts/contacts/avatar/{instance.pk}/{uuid.uuid4()}/avatar.{extension}"


class Contacts(models.Model):
    name = models.CharField(max_length=20, verbose_name="Name")
    phone = models.CharField(max_length=20, verbose_name="Phone number", blank=True)
    date_of_birth = models.DateField(
        null=True, verbose_name="Date of birth", blank=True
    )
    is_auto_generated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated date")

    avatar = models.ImageField(
        max_length=255,
        blank=True,
        null=True,
        upload_to=get_icon_path,
    )

    group = models.ForeignKey(
        Group,
        related_name="contacts_group",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
    )

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse("contacts:edit", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.name} - {self.date_of_birth}"

    __repr__ = __str__


class Meta:
    verbose_name = "Contact"
    verbose_name_plural = "Contacts"
