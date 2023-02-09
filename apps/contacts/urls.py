from django.urls import path

from apps.contacts import views

app_name = "contacts"

urlpatterns = [
    path("", views.show_all_contacts, name="index"),
    path("edit_contact/", views.show_all_to_edit, name="show_to_edit"),
    path("edit_contact/<int:pk>", views.edit_contact, name="edit"),
    path("create_contact/", views.create_contact, name="create"),
    path("delete_contact/", views.show_all_to_delete, name="show_to_delete"),
    path("delete_contact/<int:pk>/", views.ContactDeleteView.as_view(), name="delete"),
]
