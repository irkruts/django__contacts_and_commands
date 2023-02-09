from django.urls import path

from apps.contacts import views

app_name = "contacts"

urlpatterns = [
    path("", views.show_all_contacts, name="index"),
]
