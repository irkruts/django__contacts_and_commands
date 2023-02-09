# Generated by Django 4.1.1 on 2022-11-19 15:28

import apps.contacts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Contacts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20, verbose_name="Name")),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=20, verbose_name="Phone number"
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True, null=True, verbose_name="Date of birth"
                    ),
                ),
                ("is_auto_generated", models.BooleanField(default=False)),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created date"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated date"),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        max_length=255,
                        null=True,
                        upload_to=apps.contacts.models.get_icon_path,
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contacts_group",
                        to="contacts.group",
                    ),
                ),
            ],
        ),
    ]
