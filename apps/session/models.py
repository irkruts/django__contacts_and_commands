from django.db import models
from django.conf import settings


class UserDataRequest(models.Model):
    path_to_request = models.SlugField(max_length=255, verbose_name="Request path")
    session_key = models.CharField(max_length=255, verbose_name="Session key")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    counter = models.IntegerField()

    class Meta:
        verbose_name = "Users request info"
